def final(g, q1, q2):
	return round(float((g - 0.4*q1 - 0.4*q2)/0.2), 2)

q1 = float(input("Input quarter one grades --> "))
q2 = float(input("Input quarter two grades --> "))

if(input("Custom grade [Y/N]? ") == "Y"):
	grade = float(input("Input grade --> "))
	print("Final grade:", final(grade, q1, q2), "to make a", grade)
else:
	print("To pass with a 100:", final(100, q1, q2))
	print("To pass with a 90:", final(90, q1, q2))
	print("To pass with a 80:", final(80, q1, q2))
	print("To pass with a 70:", final(70, q1, q2))
	print("If the final was not taken (made a zero):", round((0.4*q1 + 0.4*q2), 2))