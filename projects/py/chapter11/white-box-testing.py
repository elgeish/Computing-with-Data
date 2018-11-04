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
  def test_put(self):
    ''' Tests put '''
    store = KeyValueStore()
    store.put('white-box', 'testing')
    self.assertEqual(store._store.get('white-box'), 'testing')


if __name__ == '__main__':
  unittest.main()
