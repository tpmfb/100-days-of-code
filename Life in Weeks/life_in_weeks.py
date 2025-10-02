def life_in_weeks():
    age = int(input("What is your current age? "))
    years_remaining = 90 - age
    days_remaining = years_remaining * 365
    weeks_remaining = years_remaining * 52
    months_remaining = years_remaining * 12

    print(f"You have {weeks_remaining} weeks left.")
    
life_in_weeks()
