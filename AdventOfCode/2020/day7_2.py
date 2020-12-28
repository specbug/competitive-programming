class Node:
	def __init__(self, color, n):
		self.color = color
		self.n = n

class Tree:
	def __init__(self, d, color, n):
		self.node = Node(color, n)
		self.children = [Node(k, v) for k, v in d[color].items()]

	def get_node(self, color):
		

	def parse_tree(self, d, color):
		for i in self.children

def temp(arr):
	d = dict()
	bags = set()
	cand = 'shiny gold'
	total = 0

	for i in arr:
		bag, temp = i.split(' bags contain ')
		contains = [i.strip() for i in temp.split(', ')]
		d[bag] = d.get(bag, {})
		bags.add(bag)
		for c in contains:
			if c.startswith('no other'):
				continue
			n, key = int(c[0]), c[1:].rstrip('bags.').rstrip('bag').strip()
			bags.add(key)
			d[bag][key] = d[bag].get(key, 0) + n
			

	print(d)


with open('day7_ip.txt', 'r') as f:
	arr = f.read().strip().split('\n')

print(temp(arr))