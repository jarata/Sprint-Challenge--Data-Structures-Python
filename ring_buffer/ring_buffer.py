class RingBuffer:
	def __init__(self, capacity):
		self.capacity = capacity
		self.current = 0
		self.storage = [None]*capacity

	def append(self, item):
		# if len(self.storage) is None:
		#   self.storage.append(item)
		# elif len(self.storage) > self.capacity:
		#   self.storage.pop(0)
		#   self.storage[1:] = self.current
		# else:
		#   self.storage
		# self.storage[self.current] = item
		# if self.current is self.capacity:
		# 	self.current-1
		if self.current == self.capacity:
			self.current = 0
		self.storage[self.current] = item
		self.current += 1

	def get(self):
		buffer = []
		for i in range(self.capacity):
			if self.storage[i]:
				buffer += self.storage[i]
		return buffer
