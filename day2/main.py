print("Welcome to the tip calculator")
total_bill = int(input("what was the total bill? $"))
tip_percent = int(
    input("How much tip would you like to give? 10, 12, or 15? "))
no_people = int(input("How many people to split the bill? "))

each_person_amount = total_bill * (1 + tip_percent/100) / no_people

print(f"Each Person should pay: ${each_person_amount:.2f}")
