def subset_sum(numbers, target, partial=[]):
    s = sum(partial)
    global g
    # check if the partial sum is equals to target
    if s == target:
        g = list(partial)

    if s >= target:
    	return

    for i in range(len(numbers)):
        n = numbers[i]
        remaining = numbers[i + 1:]
        subset_sum(remaining, target, partial + [n])

def main():
	t = int(input())
	for c in range(t):
		l = []
		o = []
		var1 = 0
		k=0
		index = []
		x, n = map(int, input().strip().split())
		l = [x1 for x1 in range(1,n+1) if x1!=x]
		s1 = [-1]*(n-1)
		s2 = ""
		if sum(l)%2!=0 or len(l)<=2:
			var1 = 1
		else:
			s = set([l[0]])
			a = ()
			n1=int(len(l)/2)
			sum1 = int(sum(l)/2)
			subset_sum(l, sum1)
			global g
			o = g[:]
			for i in l:
				if i in o:
					index.append(l.index(i))
			for i1 in range(len(l)):
				if i1 in index:
					s1[i1] =0
				else:
					s1[i1] = 1
			s1.insert(x-1, 2)
			s2 = ''.join(str(e) for e in s1)

		if var1==1:
			print("impossible")
			var1=0
		else:
			print(str(s2))

g = []
main()