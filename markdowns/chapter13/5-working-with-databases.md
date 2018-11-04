# Working with Databases

The following code creates a table, then adds two rows, and then sends
a query and displaying the results:

```python
import sqlite3
import pandas.io.sql

# create a connection
con=sqlite3.connect(':memory')
# create a table
createStmt = """
  CREATE TABLE LOCATIONS(
      ID INTEGER PRIMARY KEY,
      CITY CHAR(20),
      STATE CHAR(20),
      COUNTRY CHAR (20) NOT NULL);
"""
con.execute(createStmt)
con.commit()

# add two rows to the table
data = [(13, 'Los Angeles', 'CA', 'USA'), 
        (21, 'Chicago', 'IL', 'USA')]
addStmt = "INSERT INTO LOCATIONS VALUES (?, ?, ?, ?)"
con.executemany(addStmt, data)
con.commit()

# query the databse
data = con.execute('select * from LOCATIONS')
print(data.fetchall())
print(data.description)
```
