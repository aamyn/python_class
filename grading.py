print("Grade of Students: ")
print(input("Name: "))
marks=eval(input("Marks: "))

Grade=(" ")

if marks>80 and marks<101:
	Grade=("A1")
elif marks>70 and marks<80:
	Grade=("B2")
elif marks>65 and marks<70:
	Grade=("B3")
elif marks>60 and marks<65:
	Grade=("C4")
elif marks>55 and marks<60:
	Grade=("C5")
elif marks>50 and marks<55:
	Grade=("C6")
elif marks>45 and marks<50:
	Grade=("D7")
elif marks>40 and marks<45:
	Grade=("E8")
elif marks>0 and marks<40:
	Grade=("F9")	

print("Grade:",str(Grade))	
