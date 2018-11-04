# Test Case Anatomy - Part II

Here's an example that makes use of the `setUp` method to create a new
instance of the key-value store in a clean state for each test case:

```python runnable
import unittest

class KeyValueStore(object):
  ''' A key-value store example '''
  def __init__(self):
    self._store = {}

  def put(self, key, value):
    ''' Puts a value in the store '''
    self._store[key] = value

  def get(self, key):
    ''' Gets a value from the store by its key '''
    return self._store.get(key)


class TestKeyValueStore(unittest.TestCase):
  ''' A unit test for KeyValueStore '''
  def setUp(self):
    ''' Runs before each test method '''
    self.store = KeyValueStore()

  def test_init(self):
    ''' Tests __init__ '''
    self.assertEqual(self.store.get('key'), None)
    self.assertEqual(len(self.store._store), 0)

  def test_put_with_value(self):
    ''' Tests put '''
    self.store.put('key', 'value')
    self.assertEqual(self.store.get('key'), 'value')
    self.assertEqual(len(self.store._store), 1)

  def test_put_with_none_value(self):
    ''' Tests put with none value '''
    self.store.put('key', None)
    self.assertEqual(self.store.get('key'), None)
    self.assertEqual(len(self.store._store), 1)


if __name__ == '__main__':
  unittest.main()
```
