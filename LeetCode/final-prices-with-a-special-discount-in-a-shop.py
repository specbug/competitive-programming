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
			return None
		val = self.peek()
		self._ptop -= 1
		return val

	def peek(self):
		if len(self) == 0:
			return None
		return self._stack[self._ptop]

	def __len__(self):
		return self._ptop+1

class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        stack = Stack()
        l = len(prices)
        ans = []
        for i, n in enumerate(prices[::-1]):
            if i == 0:
                ans.append(n)
                continue
            if prices[l-i] <= n:
                stack.push(i-1)
                ans.append(n - prices[l-i])
            else:
                while stack.peek() is not None:
                    if stack.peek() == -1 or prices[l-1-stack.peek()] > n:
                        stack.pop()
                    else:
                        break
                if len(stack) == 0:
                    stack.push(-1)
                    ans.append(n)
                else:
                    ans.append(n - prices[l-1-stack.peek()])
        return ans[::-1]