from tables import *

# creating an object representing table rows
class Person(IsDescription):
  name = StringCol(16)  # 16 character string
  age = Int32Col()

# opening a HDF5 file
h5file = open_file("people.h5", mode = "w", title = "personnel")

# definining a group in the HDF4 file
group = h5file.create_group("/", "records", "names and ages")

# defining a table in the group
table = h5file.create_table(group, "Personnel1", 
                            Person, "Personnel Table 1")
Person = table.row
for ind in xrange(10):
  Person['name'] = 'John Doe ' + str(ind)
  Person['age'] = 20 + ind
  Person.append()
for ind in xrange(10):
  Person['name'] = 'Jane Smith ' + str(ind)
  Person['age'] = 20 + ind
  Person.append()
table.flush()  # update disk

# getting a pointer to table
table = h5file.root.records.Personnel1

# running a query against file
arr = [x['name'] for x in table.iterrows() if 
  x['age'] > 25 and x['age'] < 28]
print(arr)
