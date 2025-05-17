print("Welcome to the tip calculator")
bill=(float(input("What was the total bill?$\n")))
tip=(float(input("How much tip would you like to give in %?\n")))
people_splitting=(int(input("How many people are splitting the bill?\n")))
total_bill=((tip/100*bill)+bill)/people_splitting
rounded_tb=round(total_bill,2)
print(f"Each person should pay;$ {rounded_tb}")

