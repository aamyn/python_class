print("Students End of Term Result")
a=float(input("Enter the marks for Mathematics:"))
b=float(input("Enter the marks for English:"))
c=float(input("Enter the marks for Physics:"))
d=float(input("Enter the marks for Chemistry:"))
e=float(input("Enter the marks for Biology:"))
f=float(input("Enter the marks for Geography:"))
g=float(input("Enter the marks for Economics:"))
h=float(input("Enter the marks for Technical Drawing:"))
i=float(input("Enter the marks for Further Maths:"))

Total=(a+b+c+d+e+f+g+h+i)
print("Total:",str(Total))
Percentage=(Total)*(100/900)
print("Percentage:",str(Percentage))
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
marks= eval(input("Enter marks:"))
print("Grade",str(Grade))	
