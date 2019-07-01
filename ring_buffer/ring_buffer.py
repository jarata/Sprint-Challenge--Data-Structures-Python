class RingBuffer:
  def __init__(self, capacity):
    self.capacity = capacity
    self.current = 0
    self.storage = [None]*capacity

  def append(self, item):
    if len(self.storage) is None:
      self.storage.append(item)
    elif len(self.storage) > self.capacity:
      self.storage.pop(0)
      self.storage[1] = self.current
    else:
      self.storage.append(item)

  def get(self):
    return self.storage

