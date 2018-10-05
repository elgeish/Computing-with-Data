# Example 1 - single-threaded logic
def do_work():
  print('Hello, world!')

do_work()

# Example 2 - multi-threaded logic
from threading import Thread

for t in (Thread(target=do_work) for _ in range(10)):
  t.start()
