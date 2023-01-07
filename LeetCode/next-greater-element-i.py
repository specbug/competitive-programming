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
    def nextGreater(self, A):
        stack = Stack()
        max_el = -1
        for i in A:
            if i > max_el:
                max_el = i
        n = len(A)
        ans = [-1]*(max_el+1)
        for i, a in enumerate(A[::-1]):
            if i == 0:
                ans[a] = -1
                continue
            if A[n-i] > a:
                ans[a] = A[n-i]
                stack.push(n-i)
            else:
                while stack.peek() is not None:
                    if stack.peek() == -1 or A[stack.peek()] <= a:
                        stack.pop()
                    else:
                        break
                if len(stack) == 0:
                    ans[a] = -1
                else:
                    ans[a] = A[stack.peek()]
        return ans

    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        greater_map = self.nextGreater(nums2[:])
        ans = []
        for i in nums1:
            ans.append(greater_map[i])
        return ans