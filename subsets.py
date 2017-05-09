#!/usr/bin/python
import sys

def decimal_to_list_binary(n):
	return map(int,list('{0:0b}'.format(n)))

def compress(data, filter):
    return (d for d, s in izip(data, selectors) if s)
    
if __name__ == '__main__':
	print 'Give me a set of numbers:'
	original_set = raw_input()
	original_set = map(int,original_set.split())
	n = len(original_set)
	for i in range((2**n)-1):
		print bin(i)
	print (original_set,n)