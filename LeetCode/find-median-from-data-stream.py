class Heap:
	def __init__(self):
		self._heap = []
		self._len = 0

	def __repr__(self):
		return [f for f in self._heap[:self._len]].__repr__()

	def _bubble_up(self, i):
		raise NotImplementedError

	def _bubble_down(self, i):
		raise NotImplementedError

	def _get_parent_index(self, i):
		return (i-1)//2

	def _get_children_indices(self, i):
		return 2*i+1, 2*i+2

	def push(self, val):
		if self._len >= len(self._heap):
			self._heap.append(None)
		self._heap[self._len] = val
		self._bubble_up(self._len)
		self._len += 1

	def pop(self):
		if self._len == 0:
			return
		val, self._heap[0] = self._heap[0], self._heap[self._len-1]
		self._len -= 1
		self._bubble_down(0)
		return val

	def heapify(self, arr):
		self._heap = arr
		n = self._len = len(arr)
		mid = n-1-(n+1)//2
		for i in range(mid, -1, -1):
			self._bubble_down(i)

	def replace(self, val):
		if self._len == 0:
			raise IndexError
		x, self._heap[0] = self._heap[0], val
		self._bubble_down(0)
		return x

	def pushpop(self, val):
		raise NotImplementedError

	def __len__(self):
		return self._len

	def __getitem__(self, y):
		return self._heap[y]


class MaxHeap(Heap):
	def _bubble_up(self, i):
		parent_idx = self._get_parent_index(i)
		while parent_idx >= 0 and self._heap[i] > self._heap[parent_idx]:
			self._heap[i], self._heap[parent_idx] = self._heap[parent_idx], self._heap[i]
			i = parent_idx
			parent_idx = self._get_parent_index(i)

	def _bubble_down(self, i):
		left_child_idx, right_child_idx = self._get_children_indices(i)
		m = self._heap[left_child_idx] if left_child_idx < self._len else None
		n = self._heap[right_child_idx] if right_child_idx < self._len else None
		while (m is not None and m > self._heap[i]) or (n is not None and n > self._heap[i]):
			if m is None:
				swap_idx = right_child_idx
			elif n is None:
				swap_idx = left_child_idx
			else:
				if m > n:
					swap_idx = left_child_idx
				else:
					swap_idx = right_child_idx
			self._heap[i], self._heap[swap_idx] = self._heap[swap_idx], self._heap[i]
			i = swap_idx
			left_child_idx, right_child_idx = self._get_children_indices(i)
			m = self._heap[left_child_idx] if left_child_idx < self._len else None
			n = self._heap[right_child_idx] if right_child_idx < self._len else None

	def pushpop(self, val):
		if self._len == 0 or val >= self._heap[0]:
			return val
		x, self._heap[0] = self._heap[0], val
		self._bubble_down(0)
		return x

class MinHeap(Heap):
	def _bubble_up(self, i):
		parent_idx = self._get_parent_index(i)
		while parent_idx >= 0 and self._heap[i] < self._heap[parent_idx]:
			self._heap[i], self._heap[parent_idx] = self._heap[parent_idx], self._heap[i]
			i = parent_idx
			parent_idx = self._get_parent_index(i)
	
	def _bubble_down(self, i):
		left_child_idx, right_child_idx = self._get_children_indices(i)
		m = self._heap[left_child_idx] if left_child_idx < self._len else None
		n = self._heap[right_child_idx] if right_child_idx < self._len else None
		while (m is not None and m < self._heap[i]) or (n is not None and n < self._heap[i]):
			if m is None:
				swap_idx = right_child_idx
			elif n is None:
				swap_idx = left_child_idx
			else:
				if m < n:
					swap_idx = left_child_idx
				else:
					swap_idx = right_child_idx
			self._heap[i], self._heap[swap_idx] = self._heap[swap_idx], self._heap[i]
			i = swap_idx
			left_child_idx, right_child_idx = self._get_children_indices(i)
			m = self._heap[left_child_idx] if left_child_idx < self._len else None
			n = self._heap[right_child_idx] if right_child_idx < self._len else None

	def pushpop(self, val):
		if self._len == 0 or val <= self._heap[0]:
			return val
		x, self._heap[0] = self._heap[0], val
		self._bubble_down(0)
		return x

class MedianFinder:
    def __init__(self):
        self._max_heap = MaxHeap()
        self._min_heap = MinHeap()
        

    def addNum(self, num: int) -> None:
        if len(self._max_heap) == 0:
            self._max_heap.push(num)
            return
        median = self.findMedian()
        if num <= median:
            if len(self._max_heap) > len(self._min_heap):
                x = self._max_heap.replace(num)
                self._min_heap.push(x)
            else:
                self._max_heap.push(num)
        else:
            if len(self._min_heap) == len(self._max_heap):
                x = self._min_heap.pushpop(num)
                self._max_heap.push(x)
            else:
                self._min_heap.push(num)

    def findMedian(self) -> float:
        if (len(self._max_heap) + len(self._min_heap)) & 1:
            return self._max_heap[0]
        else:
            return (self._max_heap[0] + self._min_heap[0])/2
        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()