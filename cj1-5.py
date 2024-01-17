# Brent Brison
# Doctor Aguichine
# ASTR 19
# 16 January 2024

'''
Write a Python program that writes out a table of the function sin(x) vs. x, where x is tabulated between 0 and 2pi with a thousand entries. 
Follow the basic Python program structure, including a main program function.
'''

import math 

def sinVsX():
	print("Each value x represents n/1000 of 2pi, where our range is [0,2pi].")
	print("NOTE: Only printing 5 digits past decimal place.\n")
	
	print("x\tsin(x)\t")
	for i in range(1000):
		x = ((2*math.pi)/1000) * i
		print(f"{x:.5f}\t{math.sin(x):.5f}\t")

def main():
	sinVsX()

if __name__ == "__main__":
	main()