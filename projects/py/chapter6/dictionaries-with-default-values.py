from collections import defaultdict

# the default value is what int() returns: 0
d = defaultdict(int)
print(d[13])

# example: grouping elements by their respective keys
books = [  # documents to index: a list of (title, text) tuples
  ('hamlet', 'to be or not to be'),
  ('twelfth night', 'if music be the food of love'),
]
index = defaultdict(set)  # the default value is what set() returns: {}
for title, text in books:
  for word in text.split():
    # get or create the respective set
    # then add the title to it
    index[word].add(title)

from pprint import pprint  # pretty-printer (recommended for nested data)
pprint(index)
print(index['music'])  # query for documents that have the word 'music'

# example: building a trie (aka prefix tree)
words = { 'apple', 'ban', 'banana', 'bar', 'buzz' }
# a factory function/lambda expression that returns
# a defaultdict which uses it as a factory function
factory = lambda: defaultdict(factory)
trie = defaultdict(factory)
DELIMITER = '--END--'
LEAF = dict()
for word in words:
  level = trie
  for letter in word:
    level = level[letter]
  level[DELIMITER] = LEAF

def autocomplete(root, prefix, suffix=''):
  if DELIMITER in root:
    print(prefix + suffix)
  for key, value in root.items():
    autocomplete(value, prefix, suffix + key)

autocomplete(trie['b']['a'], 'ba')  # query for words that start with 'ba'
