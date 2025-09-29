print("Welcome to the tip calculator!")

total_bill = float(input("What was the total bill (in USD)? "))
tip_percent = float(input("How much tip would you like to give? 10, 12, 15 percent: "))
split = int(input("How many people to split the bill? "))

tip_multiplier = 1 + (tip_percent / 100)
final_bill = (total_bill * tip_multiplier) / split

print(f"Each person should pay: ${final_bill:.2f}")