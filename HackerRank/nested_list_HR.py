n = int(input())
l = []
n_l = []

for _ in range(n):
	name = input()
	score = float(input())
	n_l.append(score)
	l.append([name, score])

sec_min_n = sorted(list(set(n_l)))[1]

print('\n'.join([i[0] for i in sorted(l, key=lambda x: x[0]) if i[1]==sec_min_n]))


