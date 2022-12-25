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
		val = self.peek()
		self.__ptop -= 1
		return val

	def peek(self):
		if self.__ptop == -1:
			return -1
		return self.__stack[self.__ptop]

	def __len__(self):
		return self.__ptop+1

class Solution:
    def isValid(self, s: str) -> bool:
        brackets = {'}': '{', ']': '[', ')': '('}
        stack = Stack()
        if len(s) == 1:
            return False
        for c in s:
            if c in brackets.values():
                stack.push(c)
            else:
                if stack.peek() != brackets[c]:
                    return False
                stack.pop()
        return len(stack) == 0