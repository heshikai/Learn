#!/usr/bin/python


import sys

if len(sys.argv) > 1:
	a = 0 
	b = 1
	while ( b < int(sys.argv[1]) ):
		print(a,b,sep='\t')
		a = b
		b = b+1
	print(sys.argv[1])
