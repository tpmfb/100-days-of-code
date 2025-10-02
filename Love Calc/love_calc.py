def calculate_love_score():
    name1 = input("What is your name?\n").lower()
    name2 = input("What is their name?\n").lower()
    combined_names = name1 + name2

    true_score = 0
    love_score = 0

    # This single loop handles both counts
    for character in combined_names:
        if character in "true":
            true_score += 1
        if character in "love":
            love_score += 1

    true_string = str(true_score)
    love_string = str(love_score)
    true_love_score = true_string + love_string

    print(f"Love Score = {true_love_score}")

calculate_love_score()