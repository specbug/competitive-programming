def print_formatted(number):
	pad = len(str(bin(number)).lstrip('0b'))
	for i in range(1, number+1):
		print(str(i).rjust(pad)+' '+str(oct(i)).lstrip('0o').rjust(pad)+' '+str(hex(i).upper()).lstrip('0X').rjust(pad)+' '+str(bin(i)).lstrip('0b').rjust(pad))

n = int(input())
print_formatted(n)