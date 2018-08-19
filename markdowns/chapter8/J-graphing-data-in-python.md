# Graphing Data in Python

Despite the fact that R has excellent graphics capabilities, it's sometimes
desirable to graph data in another programming language. For example, when
the entire data analysis process is in Python, it may make sense to graph
the data within Python as well. Below and in the rest of this chapter, we
explore `matplotlib` — a popular Python module for graphing data.

```python
import matplotlib.pyplot as plt

# Working with figures in matplotlib
f1 = plt.figure()  # open a figure
f2 = plt.figure()  # open a second figure
plt.savefig('f2.pdf')  # save fig 2 - the active figure
plt.close(f2)
plt.savefig('f1.pdf')  # save fig 2 - the active figure
plt.close(f1)
```
