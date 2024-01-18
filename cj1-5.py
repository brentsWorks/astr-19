# Brent Brison
# Doctor Aguichine
# ASTR 19
# 16 January 2024

'''
Write a Python program that writes out a table of the function sin(x) vs. x, where x is tabulated between 0 and 2pi with a thousand entries. 
Follow the basic Python program structure, including a main program function.
'''

import math 
import numpy as np
from astropy.table import Table


def sinVsX():
	print("Each value x represents n/1000 of 2pi, where our range is [0,2pi].")
	print("NOTE: Only printing 5 digits past decimal place.\n")
	
	listX = np.array([], dtype=np.int32)
	list_sinX = np.array([], dtype=np.float32)
	for i in range(1000):
		x = (2*math.pi) * (i/1000)

		listX = np.append(listX, x)
		list_sinX = np.append(list_sinX, math.sin(x))
		
	t = Table([listX, list_sinX], names = ['x','sin(x)'])
	t.pprint_all()

def main():
	sinVsX()

if __name__ == "__main__":
	main()