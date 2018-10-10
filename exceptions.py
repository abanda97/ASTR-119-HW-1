#python exceptions let you deal with
#unexpected results

try:
	print(a)	#this will throw an exception since a is not defined
except:
	print("a is not defined")
	
#There are specific errors to help with cases
try:
	print(a)	#this will throw an exception since a is not defined
except NameError:
	print("a is still not defined")
except:
	print("something went wrong")
	
	#this will break our program
	#since a is not defined
print(a)
	
#Use a try statement to make a trial. in this case it will not work.