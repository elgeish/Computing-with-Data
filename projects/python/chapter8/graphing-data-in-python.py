import matplotlib.pyplot as plt

# Working with figures in matplotlib
f1 = plt.figure()  # open a figure
f2 = plt.figure()  # open a second figure
plt.savefig('f2.pdf')  # save fig 2 - the active figure
plt.close(f2)
plt.savefig('f1.pdf')  # save fig 2 - the active figure
plt.close(f1)
