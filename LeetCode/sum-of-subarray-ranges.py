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
    def nearest_left(self, A, smaller=True):
        stack = Stack()
        ans = []
        op_map = {True: ('<=', '>'), False: ('>=', '<')}
        for i, a in enumerate(A):
            if i == 0:
                ans.append(-1)
                continue
            if eval(f'{A[i-1]} {op_map[smaller][0]} {a}'):
                stack.push(i-1)
                ans.append(i-1)
            else:
                while stack.peek() is not None:
                    if stack.peek() == -1 or eval(f'{A[stack.peek()]} {op_map[smaller][1]} {a}'):
                        stack.pop()
                    else:
                        break
                if len(stack) == 0:
                    ans.append(-1)
                else:
                    ans.append(stack.peek())
        return ans

    def nearest_right(self, A, smaller=True):
        stack = Stack()
        ans = []
        op_map = {True: ('<', '>='), False: ('>', '<=')}
        n = len(A)
        for i, a in enumerate(A[::-1]):
            if i == 0:
                ans.append(-1)
                continue
            if eval(f'{A[n-i]} {op_map[smaller][0]} {a}'):
                ans.append(n-i)
                stack.push(n-i)
            else:
                while stack.peek() is not None:
                    if stack.peek() == -1 or eval(f'{A[stack.peek()]} {op_map[smaller][1]} {a}'):
                        stack.pop()
                    else:
                        break
                if len(stack) == 0:
                    ans.append(-1)
                else:
                    ans.append(stack.peek())
        return ans[::-1]

    def solve(self, A, smaller):
        ans = []
        n = len(A)
        left = self.nearest_left(A[:], smaller)
        right = self.nearest_right(A[:], smaller)
        for i, a in enumerate(A):
            if left[i] != -1 and right[i] != -1:
                ans.append((i-left[i])*(right[i]-i))
            elif left[i] == -1 and right[i] == -1:
                ans.append((i+1)*(n-i))
            else:
                if left[i] == -1:
                    ans.append((i+1)*(right[i]-i))
                else:
                    ans.append((i-left[i])*(n-i))
        return ans

    def subArrayRanges(self, nums: List[int]) -> int:
        ans = 0
        n = len(nums)
        min_arr = self.solve(nums[:], True)
        max_arr = self.solve(nums[:], False)
        for i in range(n):
            ans += (nums[i]*(max_arr[i]-min_arr[i]))
        return ans
