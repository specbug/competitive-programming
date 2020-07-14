def sockMerchant(n, ar):
	f_ar = {}
	n_pairs = 0

	for i in ar:
		f_ar[i] = f_ar.get(i, 0) + 1

	for j in list(f_ar.values()):
		n_pairs += j//2

	return n_pairs

ar = [1, 2, 1, 2, 1, 3, 2]
print(sockMerchant(len(ar), ar))