# postgreql query path: 
1. Connection: Connection has to be established between client and pg server
2. Parser: checks for syntax error, creates query tree
3. Rewrite: Applies rules to the query tree. In case of views, writes query tree to ge from actual table.
4. Planner/Optimizer: Creates query plan. Thi is used by Excuter to perform the operation. It finds all paths to run the query. Cost of each path is calculated. The cheapeast path is selected as query plan.
5. Executer: Goes through plan tree and retrives rows represented by plan. 