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
    def evalRPN(self, tokens: List[str]) -> int:
        stack = Stack()
        ops = {'+', '-', '*', '/'}
        ans = 0
        for e in tokens:
            if e in ops:
                op2 = stack.pop()
                op1 = stack.pop()
                ans = int(eval(f'{op1} {e} {op2}'))
                stack.push(ans)
            else:
                stack.push(int(e))
        return stack.pop()