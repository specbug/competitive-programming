class Stack:
	def __init__(self):
		self.__stack = []
		self.__ptop = -1
		self.__len = 0

	def __repr__(self):
		_repr = self.__stack[:self.__ptop+1].__repr__().strip('[').strip(']')
		return ' -> '.join(_repr.split(', ')[::-1])

	def push(self, val):
		self.__ptop += 1
		if self.__ptop >= self.__len:
			self.__stack.append(val)
			self.__len += 1
		else:
			self.__stack[self.__ptop] = val

	def pop(self):
		if len(self) == 0:
			return None
		val = self.peek()
		self.__ptop -= 1
		return val

	def peek(self):
		if len(self) == 0:
			return None
		return self.__stack[self.__ptop]

	def __len__(self):
		return self.__ptop+1

class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = Stack()
        for c in path.split('/'):
            if c in ['', '.']:
                continue
            if c == '..':
                stack.pop()
            else:
                stack.push(c)
        dirs = [stack.pop() for _ in range(len(stack))]
        if len(dirs) == 0:
            dirs = ['']
        return ''.join(f'/{d}' for d in dirs[::-1])