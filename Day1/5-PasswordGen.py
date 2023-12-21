#Password Generator Project
import random
letters_list = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
symbols_list = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
numbers_list = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

num_letters= len(letters_list) 
num_symbols = len(symbols_list)
num_numbers = len(symbols_list)

print("Welcome to the PyPassword Generator!")
tot_letters = int(input("How many letters would you like in your password?\n")) 
req_symbols = int(input(f"How many symbols would you like?\n"))
req_numbers = int(input(f"How many numbers would you like?\n"))
req_letters = tot_letters - (req_numbers + req_symbols)
password = ""

def add_letter():
    global password, req_letters, req_symbols
    if req_letters > 0:
        password += letters_list[random.randint(0, num_letters-1)]
        req_letters -= 1
    elif req_symbols > 0:
        add_symbol()
    else:
        add_number()


def add_symbol():
    global password, req_symbols
    if req_symbols>0:
        password += symbols_list[random.randint(0, num_symbols-1)]
        req_symbols -= 1
    else:
        add_letter()

def add_number():
    global password, req_numbers
    if req_numbers>0:
        password += numbers_list[random.randint(0, num_numbers-1)]
        req_numbers -= 1
    else:
        add_letter()

for i in range(0, int(tot_letters)):
    if req_symbols>0 or req_numbers>0:
        rand_chooser = random.randint(0,2)
        if rand_chooser == 1:
            add_letter()
        elif rand_chooser == 2:
            add_symbol()
        else:
            add_number()
    else:    
        password += letters_list[random.randint(0, num_letters-1)]

print(f"Your password is: {password}")

#Another simpler way to do this is to add all the charecters, symbols and numbers to a list then use list.shuffle() to randomize the order