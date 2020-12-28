def temp(arr):
	tree = dict()
	bags = set()
	candidates = set()

	for i in arr:
		bag, temp = i.split(' bags contain ')
		contains = [i.strip() for i in temp.split(', ')]
		tree[bag] = tree.get(bag, {})
		bags.add(bag)
		for c in contains:
			if c.startswith('no other'):
				continue
			n, key = int(c[0]), c[1:].rstrip('bags.').rstrip('bag').strip()
			bags.add(key)
			tree[bag][key] = tree[bag].get(key, 0) + n
			

	len_c = 0
	while True:
		for i in tree.keys():
			if 'shiny gold' in tree[i].keys() or len(candidates & set(tree[i].keys()))>0:
				candidates.add(i)

		if len(candidates) == len_c:
			break
		else:
			len_c = len(candidates)

	return len(candidates)

		

		

with open('day7_ip.txt', 'r') as f:
	arr = f.read().strip().split('\n')

print(temp(arr))