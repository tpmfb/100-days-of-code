import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
num_of_letters = input("How many letters would you like in your password?\n")
num_of_symbols = input("How many symbols would you like?\n")
num_of_numbers = input("How many numbers would you like?\n")

password_list = []
for l in range(1, int(num_of_letters) + 1):
    password_list.append(random.choice(letters))
for s in range(1, int(num_of_symbols) + 1):
    password_list.append(random.choice(symbols))
for n in range(1, int(num_of_numbers) + 1): 
    password_list.append(random.choice(numbers))
    
random.shuffle(password_list)
print(f"Your password is: {''.join(password_list)}")