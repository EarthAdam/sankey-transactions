# sankey-budget
A way to create quick budget overviews, like the one shared on `r/dataisbeautiful` [here](https://www.reddit.com/r/dataisbeautiful/comments/otxlbo/apples_latest_quarter_visualized_oc/).

**1. Produce a list of all transactions**<br>
[transactions.csv](transactions.csv)<br>
(This is just something you have to do manually on your bank's site )<br><br>

**2. Manually create SOURCE and TARGET values for each transaction**<br>
[accounts.csv](accounts.csv)<br> (Also something you just have to manually create for now)<br><br>

**3. Summarizing transactions**<br>
See [this post](https://stackoverflow.com/questions/72842595/python-sum-values-between-unique-pairs-in-ledger-using-hash-tables-or-dictiona?fbclid=IwAR1J4sLWwSZ6j3kU-jo7afdOqA301bB8v9WEm7YgbdrWBb_DlstV-RbkyOY) in StackOverflow for progression of approaches to summarize values<br><br>

**4. Run the code**<br>
`python budget.py`<br>
And open the resulting [index.html](index.html)
![](appleplot.png)
