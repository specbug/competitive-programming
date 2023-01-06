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
    def nearest_left(self, A):
        stack = Stack()
        ans = []
        for i, a in enumerate(A):
            if i == 0:
                ans.append(-1)
                continue
            if A[i-1] < a:
                stack.push(i-1)
                ans.append(i-1)
            else:
                while stack.peek() is not None:
                    if stack.peek() == -1 or A[stack.peek()] >= a:
                        stack.pop()
                    else:
                        break
                if len(stack) == 0:
                    ans.append(-1)
                else:
                    ans.append(stack.peek())
        return ans

    def nearest_right(self, A):
        stack = Stack()
        ans = []
        n = len(A)
        for i, a in enumerate(A[::-1]):
            if i == 0:
                ans.append(-1)
                continue
            if A[n-i] < a:
                ans.append(n-i)
                stack.push(n-i)
            else:
                while stack.peek() is not None:
                    if stack.peek() == -1 or A[stack.peek()] >= a:
                        stack.pop()
                    else:
                        break
                if len(stack) == 0:
                    ans.append(-1)
                else:
                    ans.append(stack.peek())
        return ans[::-1]

    def largestRectangleArea(self, heights: List[int]) -> int:
        ans = -1
        n = len(heights)
        left = self.nearest_left(heights[:])
        right = self.nearest_right(heights[:])
        for i, a in enumerate(heights):
            if left[i] != -1 and right[i] != -1:
                ans = max(ans, a*(right[i]-left[i]-1))
            elif left[i] == -1 and right[i] == -1:
                ans = max(ans, a*n)
            else:
                if left[i] == -1:
                    ans = max(ans, a*right[i])
                else:
                    ans = max(ans, a*(n-left[i]-1))
        return ans