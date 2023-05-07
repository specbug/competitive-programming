# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Heap:
	def __init__(self):
		self._heap = []
		self._len = 0

	def __repr__(self):
		return [f.val for f in self._heap[:self._len]].__repr__()

	def _bubble_up(self, i):
		raise NotImplementedError

	def _bubble_down(self, i):
		raise NotImplementedError

	def _get_parent_index(self, i):
		return (i-1)//2

	def _get_children_indices(self, i):
		return 2*i+1, 2*i+2

	def add(self, node):
		if self._len >= len(self._heap):
			self._heap.append(None)
		self._heap[self._len] = node
		self._bubble_up(self._len)
		self._len += 1

	def get(self):
		if self._len == 0:
			return
		node, self._heap[0] = self._heap[0], self._heap[self._len-1]
		self._len -= 1
		self._bubble_down(0)
		return node

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
		while parent_idx >= 0 and self._heap[i].val < self._heap[parent_idx].val:
			self._heap[i], self._heap[parent_idx] = self._heap[parent_idx], self._heap[i]
			i = parent_idx
			parent_idx = self._get_parent_index(i)
	
	def _bubble_down(self, i):
		left_child_idx, right_child_idx = self._get_children_indices(i)
		m = self._heap[left_child_idx].val if left_child_idx < self._len else None
		n = self._heap[right_child_idx].val if right_child_idx < self._len else None
		while (m is not None and m < self._heap[i].val) or (n is not None and n < self._heap[i].val):
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
			m = self._heap[left_child_idx].val if left_child_idx < self._len else None
			n = self._heap[right_child_idx].val if right_child_idx < self._len else None


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
	def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
		heap = MinHeap()
		heap.heapify([l for l in lists if l is not None])
		if heap.len() == 0:
			return
		curr = heap.get()
		head = merged = curr
		curr = curr.next
		if curr is not None:
			heap.add(curr)
		while heap.len() != 0:
			curr = heap.get()
			merged.next = curr
			merged = merged.next
			curr = curr.next
			if curr is not None:
				heap.add(curr)
		return head