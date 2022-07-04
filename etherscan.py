# https://api.etherscan.io/api?module=account&action=txlist&address=0x34BD8A7AE5369B71380B88157e01372182A10638&startblock=0&endblock=99999999&page=1&offset=10&sort=asc&apikey=ZQJQDAY6SGPA5GN5XBDMPH65MTCD2FZNSI
# See Docs here: https://docs.etherscan.io/api-endpoints/accounts
from urllib.request import urlopen
import json
from tabulate import tabulate
import plotly.graph_objects as go
import numpy as np

#url = 'https://api.etherscan.io/api?module=account&action=txlist&address=0x34BD8A7AE5369B71380B88157e01372182A10638&startblock=0&endblock=99999999&page=1&offset=10&sort=asc&apikey=ZQJQDAY6SGPA5GN5XBDMPH65MTCD2FZNSI'
#response = urlopen(url)

xs = open('transactions.json')
x = json.loads(xs.read())

transactions = []
for y in x["result"]:
    if(int(y["value"])!=0):
        transactions.append([y['from'],y['to'],'{:f}'.format(float(y["value"])/1000000000000000000)])

# Get array of Column
def column(matrix, i):
    return [row[i] for row in matrix]

sources = column(transactions,0)
targets = column(transactions,1)
values = column(transactions,2)

# Create a dictionary of totals between accounts
d = dict.fromkeys(zip(sources, targets), 0)
for s, t, v in zip(sources, targets, values): d[(s, t)] += float(v)

# Convert dict to parallel arrays
totals = []
for value in d:
    totals.append([value[0],value[1],float(d[(value[0],value[1])])])

# Update to summarized lists
new_sources = column(totals,0)
new_targets = column(totals,1)
new_values = column(totals,2)

print(new_sources)
print(new_targets)
print(new_values)

# print(tabulate(transactions))
print(tabulate(totals))

#Configure diagram
fig = go.Figure(data=[go.Sankey(
    node = dict(
      pad = 15,
      thickness = 20,
      line = dict(color = "black", width = 0.5)
    ),
    link = dict(
      source = new_sources,
      target = new_targets,
      value = new_values
  ))])
fig.update_layout(title_text="Transactions with account: 0x34BD8A7AE5369B71380B88157e01372182A10638", font_size=10)
fig.show()
fig.write_html('index.html')