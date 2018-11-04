# Gray-Box Testing

Here's an example of testing the `put` method of our key-value store
in a scenario that requires some knowledge about how the store is implemented
to verify the post-conditions of the method:

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
  def test_put_key_already_exists(self):
    ''' Tests put when key already exists '''
    store = KeyValueStore()
    store.put('same key twice', 'first time')
    store.put('same key twice', 'second time')
    # This a black-box assertion
    self.assertEqual(store.get('same key twice'), 'second time')
    self.assertEqual(len(store._store), 1)  # a white-box one


if __name__ == '__main__':
  unittest.main()
```
