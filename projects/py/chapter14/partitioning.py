N = 5
counts = [0 for i in range(N)]
for email in open('chapter14/enron.txt'):
  counts[hash(email.rstrip()) % N] += 1
print(counts)
