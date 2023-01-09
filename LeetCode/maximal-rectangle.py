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
        ans = []
        stack = Stack()
        n = len(A)
        for i in range(n):
            if i == 0:
                ans.append(-1)
                continue
            if A[i] > A[i-1]:
                stack.push(i-1)
                ans.append(i-1)
            else:
                while stack.peek() is not None:
                    if stack.peek() == -1 or A[i] <= A[stack.peek()]:
                        stack.pop()
                    else:
                        break
                if len(stack) == 0:
                    ans.append(-1)
                else:
                    ans.append(stack.peek())
        return ans


    def nearest_right(self, A):
        ans = []
        stack = Stack()
        n = len(A)
        for i in range(n-1, -1, -1):
            if i == n-1:
                ans.append(-1)
                continue
            if A[i] > A[i+1]:
                stack.push(i+1)
                ans.append(i+1)
            else:
                while stack.peek() is not None:
                    if stack.peek() == -1 or A[i] <= A[stack.peek()]:
                        stack.pop()
                    else:
                        break
                if len(stack) == 0:
                    ans.append(-1)
                else:
                    ans.append(stack.peek())
        return ans[::-1]

    def get_length(self, x, y, t):
        if x != -1 and y != -1:
            l = y-x-1
        elif x == y == -1:
            l = t
        else:
            if x == -1:
                l = y
            else:
                l = t-x-1
        return l

    def get_max_area(self, A):
        ans = 0
        n = len(A)
        left = self.nearest_left(A[:])
        right = self.nearest_right(A[:])
        for i in range(n):
            l = self.get_length(left[i], right[i], n)
            ans = max(ans, A[i]*l)
        return ans

    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        n = len(matrix)
        m = len(matrix[0])
        hist = [0]*m
        ans = 0
        for i in range(n):
            for j in range(m):
                if matrix[i][j] == '1':
                    hist[j] += 1
                else:
                    hist[j] = 0
            ans = max(ans, self.get_max_area(hist[:]))
        return ans