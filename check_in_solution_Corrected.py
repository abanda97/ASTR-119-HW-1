#include the Numpy Library
import numpy as np

#define the main() function
def main() :

	i = 0			#declare an integer i
	x = 119.0		#declare a float x
	
	for i in range(120) :		#loop i from 0 to 119, inclusive
	
		if((i%2)==0) :			#if i is even
			#I originally had x =+ 3.0 but that is wrong
			x += 3.0				#add 3 to x
		else:
			x -= 5.0			#if i is odd, subtract 5 from x
			
	s = "%3.2e" % x				#make a string containing x with
								#scientific notation w/ 2 decimal places
								
	print (s)					#print s to the screen
	
	

#now the rest of the program continues

if __name__ == "__main__":		#if the main() function exists, run it
	main()