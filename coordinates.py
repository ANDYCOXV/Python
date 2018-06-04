#Author: Andy Cox V
#Date: 12/3/2017
#Programming Language: Python
#Name: function.py
#This program prints out the y value of the function with x as the input.

#Used to check if the user input is a floating point number.
#Returns True if it is a float returns False if not.
def isFloat(a):
        try:
                float(a)
                return True
        except:
                return False

#Opening prompt.                     
print("\nfunction.py - Andy Cox V - Copyright (c) 12/3/2017\n"
	+ "Calculates the y value given the x value of the function:\n(x^2 - 4)/(x^4 - 10 * x^2 + 9)")

#Program loop.
while(True):
	x = input("\nInput an x-coordinate <Press 'q' to exit> --> ") #Aquire user input and check for errors.

	if(isFloat(x) == True):
		x = float(x)
		try:
			print("(" + str(x) + "," + str((x ** 2 - 4)/(x ** 4 - 10 * x ** 2 + 9)) + ")") #Print out the computation.
		except:
			print("COMPUTATION ERROR: Cannot preform division by zero!")
	elif((isFloat(x) == False) and (x == "q")):
		quit()
	else:
		print("INPUT ERROR: Floating point numbers only!")