#!/usr/bin/python
import sys
from itertools import izip

def decimal_to_list_binary(n,t):
	return map(int,str('{0:0'+str(t)+'b}').format(n))

def compress(data, filter):
    return (d for d, s in izip(data, filter) if s)

if __name__ == '__main__':
	print 'Give me a set of numbers:'
	original_set = raw_input()
	original_set = map(int,original_set.split())
	n = len(original_set)
	subsets=[]
	for i in range((2**n)):
		filt = decimal_to_list_binary(i,n)
		a= compress(original_set,filt)
		subsets.append(list(a))
	for subset in subsets:
		print (subset)