# Window Functions in Postgresql

- Window functions perform calculations across sets of rows related to current row. 
- eg Get the salary of employee and comapre it with dept avg salary

- This is very similar to aggregate functions. the main difference is with aggregate functions the results are grouped into single row, and the context with each individual row cannot be established. The window functions retain their own seperate identities.
- eg Aggregate functions can be used to get avg department salary. But it cant be easily compared with individual salary of each employee.

- Example
```sql
SELECT depname, empno, salary, avg(salary) OVER (PARTITION BY depname) FROM empsalary;
```

- in above example `avg() OVER ()` is a window function which is opertating on window `(PARTITION BY depname)`

- The `PARTITION BY` clause in `OVER` divides the row into groups or partitions. Order of the recors in window can controlled using `ORDER BY` clause within `OVER`.

- If query has any window functions then they will be performed after `grouping`, `aggregation`, and `HAVING` filtering is performed. In this case the rows seen by window functions are group rows and not rows returned by `FROM`/`WHERE`

- Window funtions are only permitted in `SELECT` list and `ORDER BY` clause of query. They are forbidden elsewhere, such as in `GROUP BY`, `HAVING` and `WHERE` clauses.As these clauses are executed first

- All the window functions can be found (here)[https://www.postgresql.org/docs/current/functions-window.html#FUNCTIONS-WINDOW-TABLE]

- Any built in or user defined aggregte functions can be used as window functions. Aggregate functions act as Window functions only if `**OVER**` follows the direct function call.

## Sources

1. (Window Functions Tutorial)[https://www.postgresql.org/docs/current/tutorial-window.html]
2. (Window Functions List)[https://www.postgresql.org/docs/current/functions-window.html#FUNCTIONS-WINDOW-TABLE]
3. Window Functions Processing[https://www.postgresql.org/docs/current/queries-table-expressions.html#QUERIES-WINDOW]