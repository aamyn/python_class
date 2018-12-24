print("Compute the grade of a student")
name=input("Enter your name: ")
marks=eval(input("Enter marks: "))
grade=(" ")

if marks>70 and marks<101:
	grade=("A")
	
elif marks>60 and marks<70:
	grade=("B")
	
elif marks>50 and marks<60:
	grade=("C")
	
elif marks>40 and marks<50:
	grade=("D")
	
elif marks>35 and marks<40:
	grade=("E")
	
elif marks<35:
	grade=("fail")
	
print("Grade: ", str(grade))	
