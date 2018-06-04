#Author: Andy Cox V
#Date: 12/3/2017
#Programming Language: Python
#Name: trapezoidrule.py
#This program preforms the trapezoid rule to find the area underneath the curve.
#Trapazoid Rule: (dx / 2)[f(x0) + 2 * f(x1) + 2 * f(x2) + ... + f(xn)]

#Note: Keep the ".0" suffix on every number to denote that it is floating point number.
b = 0.0         #Upper bound.
a = 0.0         #Lower bound.
n = 0.0         #Number of cuts.
dx = 0.0        #Delta x.
ans = 0.0       #Answer used for the computations.
i = 1.0         #Must be set to one!
fun = "(x ** 2 - 4)/(x ** 4 - 10 * x ** 2 + 9)" #Change this function to preform the computations -- MUST KEEP "x" AS THE VARIABLE!

#Used to check if the user input is a floating point number.
#Returns True if it is a float returns False if not.
def isFloat(a):
        try:
                float(a)
                return True
        except:
                return False

#Used to aquire the bounds for the Trapazoid Rule.
#Returns a floating point number.
def getBound(comment):
        while(True):
                x = input(comment)
                if(isFloat(x)):
                        x = float(x)
                        try:
                                eval(fun)
                                return x
                        except:
                                print("COMPUTATION ERROR: The bound is not on the closed interval!")
                elif((not isFloat(x)) and (x == "q")):
                        quit()
                else:
                        print("INPUT ERROR: Floating point numbers only!")

#Used to get general floating point numbers.
#Returns a floating point number.
def getFloat(comment):
        while(True):
                x = input(comment)
                if(isFloat(x)):
                        return float(x)
                elif((not isFloat(x)) and (x == "q")):
                        quit()
                else:
                        print("INPUT ERROR: Floating point numbers only!")

#Used to compute the function.
#Returns a floating point number.
def compute(x):
        return float(eval(fun))

#Used to compute the argument for the function during the computations for the Trapazoid Rule.
#Returns a floating point number.
def argument(a, dx, i):
        return float(a + (dx * i))

#Opening prompt.        
print("\ntrapezoidrule.py - Andy Cox V - Copyright (c) 12/3/2017\n"
	+ "Calculates the area under the curve using the trapezoid rule of the function:\n" + fun
        + "\nTrapezoid Rule: (dx / 2)[f(x0) + 2 * f(x1) + 2 * f(x2) + ... + f(xn)]")

#User input loop for the computation and other possible computations.
while(True):
        #Aquire the user inputs.
        a = getBound("\nInput the lower bound (a) <Press 'q' to quit> --> ")
        b = getBound("\nInput the upper bound (b) <Press 'q' to quit> --> ")
        n = getFloat("\nInput the number of cuts to preform (n) <Press 'q' to quit> --> ")

        dx = (b - a) / n #Delta x of the trapezoid rule.
        
        print("\n\nTrapezoid Rule for the function: " + fun + "\nComputations:\n") #Shows the listing of computations and function to preform. 
        
        print("(" + str(dx) + " / 2)\n[\nf(" + str(a) + ")") #First function to compute.
        ans += compute(a)
        
        #All other computations that require 2 * f(x).
        while(i < n):
                print("+ 2 * f(" + str(argument(a, dx, i)) + ")")
                ans += 2 * compute(argument(a, dx, i))
                i += 1

        print("+ f(" + str(b) + ")\n]") #Last function to compute.
        ans += compute(b)
        ans *= dx / 2
        
        #Print out of all of the attributes for the Trapazoid Rule.
        print("\nTrapezoid Rule for the function: " + fun + "\nOn the closed interval: [" + str(a) + "," + str(b) + "]\n")
        print("Lower bound (a):", a)
        print("Upper bound (b):", b)
        print("Number of cuts:", n)
        print("Delta x (" + str(b) + " - " + str(a) + ") / " + str(n) + ":", dx)
        print("Area under the curve:", ans)
        
        #Reset these variables for the next set of computations.
        i = 1 #i MUST EQUAL 1!
        ans = 0 #ans MUST EQUAL 0!
        
        if(input("\nPress any key to compute or press 'q' to quit... ") == "q"): #Check if the user would like to terminate the program.
                quit()