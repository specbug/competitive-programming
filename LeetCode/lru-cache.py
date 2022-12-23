class Node:
	def __init__(self, val):
		self.val = val
		self.prev = None
		self.next = None

class LinkedList:
	def __init__(self):
		self.head = None
		self.tail = None
		self._len = 0

	def add(self, val):
		self._len += 1
		node = Node(val)
		if not self.head:
			self.head = node
			return node
		if not self.tail:
			self.tail = node
			self.head.next = self.tail
			self.tail.prev = self.head
			return node
		node.prev = self.tail
		self.tail.next = node
		self.tail = node
		return node

	def remove(self, node):
		self._len -= 1
		if node is self.head:
			self.head = self.head.next
			if self.head:
				self.head.prev = None
		elif node is self.tail:
			self.tail = self.tail.prev
			if self.tail:
				self.tail.next = None
		else:
			node.prev.next = node.next
			node.next.prev = node.prev

	def peek(self):
		if self._len == 0:
			return -1
		return self.head.val

	def get_head(self):
		return self.head

	def __len__(self):
		return self._len


class LRUCache:
	def __init__(self, capacity):
		self.capacity = capacity
		self._map = dict()
		self._cache = LinkedList()

	def __repr__(self):
		_repr = '='*10
		# _repr += f'Map:\n{self._map}'
		_repr += '\nCache:\n'
		temp = self._cache.get_head()
		if temp:
			_repr += str(temp.val)
			temp = temp.next
			while temp:
				_repr += f' -> {temp.val}'
				temp = temp.next
		_repr += '\n'
		_repr += '='*10
		return _repr

	def get(self, key):
		if key not in self._map:
			return -1
		node = self._map[key]
		self._cache.remove(node)
		new_node = self._cache.add(node.val)
		self._map[key] = new_node
		return new_node.val

	def put(self, key, value):
		if key in self._map:
			self._cache.remove(self._map[key])
		else:
			if len(self._cache) == self.capacity:
				node = self._cache.get_head()
				self._cache.remove(node)
				for k, v in self._map.items():
					if v is node:
						del self._map[k]
						break
		new_node = self._cache.add(value)
		self._map[key] = new_node
