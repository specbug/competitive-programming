class Queue:
	def __init__(self):
		self._queue = []
		self._ptop = 0
		self._len = 0

	def __repr__(self):
		_repr = self._queue[self._ptop:].__repr__().strip('[').strip(']')
		return ' -> '.join(_repr.split(', '))

	def enqueue(self, val):
		self._len += 1
		self._queue.append(val)

	def __clear(self):
		self._queue = []
		self._ptop = 0
		self._len = 0

	def dequeue(self):
		val = self._queue[self._ptop]
		self._ptop += 1
		if self._ptop == self._len:
			self.__clear()
		return val

	def pop(self):
		val = self._queue.pop()
		self._len -= 1
		if self._ptop == self._len:
			self.__clear()
		return val

	def peek(self):
		if len(self) == 0:
			return None
		return self._queue[self._ptop]

	def peek_last(self):
		if len(self) == 0:
			return None
		return self._queue[self._len-1]

	def is_empty(self):
		return len(self) == 0

	def __len__(self):
		return self._len - self._ptop

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        if k == 1:
            return nums
        n = len(nums)
        if n == 1:
            return nums[0]
        k = min(n, k)
        queue = Queue()
        ans = []
        for i in range(k):
            while not queue.is_empty() and nums[i] > nums[queue.peek_last()]:
                queue.pop()
            queue.enqueue(i)
        ans.append(nums[queue.peek()])

        for i in range(n-k):
            if queue.peek() == i:
                queue.dequeue()
            while not queue.is_empty() and nums[i+k] > nums[queue.peek_last()]:
                queue.pop()
            queue.enqueue(i+k)
            ans.append(nums[queue.peek()])
        return ans