#Exponents can be done with **
print("Exponent calc of 2^5: " + str(2**4))
print("Rounding 16/5 = 3.2 becomes " + str(round(16/5)))
print("Rounding 8/3 = 2.666... rounded 2 decimal point becomes " + str(round(8/3, 2)))
print()

#TipCalc
print("Welcome to the tip calculator app.")
total_bill = float(input("What was the total bill? $"))
num_people = int(input("How many people are splitting the bill? "))
tip_percentage = float(input("What is the percentage of tip you want to give? "))
total_tip = total_bill * (tip_percentage/100)
bill_per_person = (total_bill + total_tip) / num_people
print(f"Each person needs to pay ${bill_per_person}")
print("End of tip calculator.")
