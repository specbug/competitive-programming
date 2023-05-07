class Heap:
	def __init__(self):
		self._heap = []
		self._len = 0

	def __repr__(self):
		return [f[1] for f in self._heap[:self._len]].__repr__()

	def _bubble_up(self, i):
		raise NotImplementedError

	def _bubble_down(self, i):
		raise NotImplementedError

	def _get_parent_index(self, i):
		return (i-1)//2

	def _get_children_indices(self, i):
		return 2*i+1, 2*i+2

	def add(self, coord):
		if self._len >= len(self._heap):
			self._heap.append(None)
		self._heap[self._len] = coord
		self._bubble_up(self._len)
		self._len += 1

	def get(self):
		if self._len == 0:
			return
		coord, self._heap[0] = self._heap[0], self._heap[self._len-1]
		self._len -= 1
		self._bubble_down(0)
		return coord

	def heapify(self, arr):
		self._heap = arr
		n = self._len = len(arr)
		mid = n-1-(n+1)//2
		for i in range(mid, -1, -1):
			self._bubble_down(i)

	def len(self):
		return self._len


class MinHeap(Heap):
	def _bubble_up(self, i):
		parent_idx = self._get_parent_index(i)
		while parent_idx >= 0 and self._heap[i][1] < self._heap[parent_idx][1]:
			self._heap[i], self._heap[parent_idx] = self._heap[parent_idx], self._heap[i]
			i = parent_idx
			parent_idx = self._get_parent_index(i)
	
	def _bubble_down(self, i):
		left_child_idx, right_child_idx = self._get_children_indices(i)
		m = self._heap[left_child_idx][1] if left_child_idx < self._len else None
		n = self._heap[right_child_idx][1] if right_child_idx < self._len else None
		while (m is not None and m < self._heap[i][1]) or (n is not None and n < self._heap[i][1]):
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
			m = self._heap[left_child_idx][1] if left_child_idx < self._len else None
			n = self._heap[right_child_idx][1] if right_child_idx < self._len else None


class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        coords = []
        ans = []
        heap = MinHeap()
        for i in points:
            x, y = i
            coord = ((x, y), (x**2+y**2)**(1/2))
            coords.append(coord)
        heap.heapify(coords)
        while k:
            coord, _ = heap.get()
            ans.append(coord)
            k -= 1
        return ans