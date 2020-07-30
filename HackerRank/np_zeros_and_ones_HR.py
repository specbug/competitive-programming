import numpy as np

def print_array(shape):
	print(np.zeros(shape, dtype='int'))
	print(np.ones(shape, dtype='int'))
	return

shape = tuple(map(int, input().split()))
print_array(shape)