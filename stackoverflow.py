from tabulate import tabulate

sources = ['A','A','A','A','A','B','B','B','B']
targets = ['C','C','C','D','D','C','C','D','D']
values =  [ 2 , 1 , 2 , 2 , 3 , 2 , 3 , 2 , 3 ]

# Create a dictionary of totals between accounts
d = dict.fromkeys(zip(sources, targets), 0)
for s, t, v in zip(sources, targets, values): d[(s, t)] += v

# Convert dict to parallel arrays
totals = []
for value in d:
    totals.append([value[0],value[1],d[(value[0],value[1])]])
print(tabulate(totals))