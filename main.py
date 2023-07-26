print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? \n"))
tip = int(input("What percentage tip would you like to give? \n"))
people = int(input("How many people to slpit the bill? \n"))
bill_with_tip = tip / 100 * bill + bill
bill_per_person = round(bill_with_tip / people, 2)
bill_per_person = "{0:.2f}".format(bill_per_person)
#print("Amount per person is: " + str(bill_per_person))
print(f"Each person should pay: ${bill_per_person}")
