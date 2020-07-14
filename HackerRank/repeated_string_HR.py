def repeatedString(s, n):
	
	n_a = len([i for i in s if i=='a'])
	n_a = (n//len(s))*n_a

	if n%len(s) != 0:
		n_a += len([i for i in s[:(n-len(s)*(n//len(s))):] if i=='a'])

	return n_a


s = 'aba'
n = 14

print(repeatedString(s, n))