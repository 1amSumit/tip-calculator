print("Wellcome to the tip calculator")
totalAmount = input("What is your total bill Amount ? : $")
tippercentage = input("What percentage tip would you like to give : 10% 12% 15% 20% ")
split =input("How many people to split the bill into?")
person = int(split)
totalBill = int(totalAmount)
tipPer = int(tippercentage)
tip = round(((totalBill*tipPer)/100) , 2 )
totalBill = totalBill + tip 
eachPay = totalBill / person
print(f"Each person  should pay : ${eachPay}")