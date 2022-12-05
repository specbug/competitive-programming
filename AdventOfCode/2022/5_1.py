import re
import sys

class Stack:
	def __init__(self):
		self._stack = []
		self._len = -1

	def __repr__(self):
		return ' '.join([str(i) for i in self._stack])

	def push(self, val):
		self._stack.append(val)
		self._len += 1

	def pop(self):
		if self._len == -1:
			raise IndexError(f'Can\'t remove from an empty stack.')
		return self._stack.pop()

	def peek(self):
		return self._stack[-1]

	def is_empty(self):
		return self._len == -1

	def __len__(self):
		return self._len

def main(file):
	ans = 0
	with open(file) as f:
		n_stacks_arr = []
		stacks = []
		stack_map = dict()
		read_stack = False
		for l in f.readlines():
			if l.strip() == '':
				assert all(len(n_stacks_arr) == len(_garbx:=st) for st in stacks), f'{_garbx} doesn\'t match the total stacks ({len(n_stacks_arr)})'
				for e, st in enumerate(list(zip(*stacks))):
					_st = Stack()
					for v in st[::-1]:
						if v:
							_st.push(v)
					stack_map[e+1] = _st
				read_stack = True
				continue
			if read_stack:
				n, posx, posy = tuple(map(int, re.findall(r'move (\d+) from (\d+) to (\d+)', l.strip('\n'))[0]))
				for _ in range(n):
					val = stack_map[posx].pop()
					stack_map[posy].push(val)
			else:
				st = []
				alt = 0
				for c in l.strip('\n'):
					if c.startswith(('[', ']')):
						continue
					if c == ' ':
						alt += 1
						if alt <= 3:
							continue
					if c.isalnum():
						if c.isalpha():
							st.append(c)
						else:
							n_stacks_arr.append(int(c))
					else:
						st.append(None)
					alt = 0
				if len(st) > 0:
					stacks.append(st)
		ans = ''.join(str(st.peek()) for st in stack_map.values())
	return ans


file = sys.argv[1]
print(main(file))