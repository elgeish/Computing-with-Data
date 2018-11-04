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

    # Set up
    store = KeyValueStore()
    store.put('same key twice', 'first time')

    # Execute
    store.put('same key twice', 'second time')
    
    # Verify
    self.assertEqual(store.get('same key twice'), 'second time')
    self.assertEqual(len(store._store), 1)

    # No shared state between tests => no cleanup required


if __name__ == '__main__':
  unittest.main()
