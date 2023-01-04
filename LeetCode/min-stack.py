class Stack:
	def __init__(self):
		self._stack = []
		self._ptop = -1
		self._len = 0

	def __repr__(self):
		_repr = self._stack[:self._ptop+1].__repr__().strip('[').strip(']')
		return ' -> '.join(_repr.split(', ')[::-1])

	def push(self, val):
		self._ptop += 1
		if self._ptop >= self._len:
			self._stack.append(val)
			self._len += 1
		else:
			self._stack[self._ptop] = val

	def pop(self):
		if len(self) == 0:
			return -1
		val = self.peek()
		self._ptop -= 1
		return val

	def peek(self):
		if len(self) == 0:
			return -1
		return self._stack[self._ptop]

	def __len__(self):
		return self._ptop+1

class MinStack(Stack):
	def __init__(self):
		super().__init__()
		self._min = Stack()

	def push(self, val):
		super().push(val)
		if len(self._min) == 0 or val <= self._min.peek():
			self._min.push(val)

	def pop(self):
		val = super().pop()
		if val == self._min.peek():
			self._min.pop()

	def top(self):
		return super().peek()

	def getMin(self):
		return self._min.peek()


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()