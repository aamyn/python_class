print("create new bill")
amount=float(input("enter amount: "))
if amount<1000:
	discount=amount*(5/100)
	print("Discount",discount)
else:
	discount=amount*(10/100)
	print("Discount",discount)
print("Net payable: ",amount-discount)
