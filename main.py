# This is Day 5 of 100 for the Udemy Python Bootcamp
import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to Aaron's PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91

easy_password = ""

for character in range(1, nr_letters +1):
    easy_password += random.choice(letters)

for symbol in range(1, nr_symbols +1):
    easy_password += random.choice(symbols)

for number in range(1, nr_numbers +1):
    easy_password += random.choice(numbers)

print(f"Your new EASYMODE password is {easy_password})")

#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P

complex_password = []

for character in range(1, nr_letters +1):
    complex_password += random.choice(letters)

for symbol in range(1, nr_symbols +1):
    complex_password += random.choice(symbols)

for number in range(1, nr_numbers +1):
    complex_password += random.choice(numbers)

random.shuffle(complex_password)

new_complex_password = ""
for char in complex_password:
    new_complex_password += char

print(f"Your new HARDMODE password is {new_complex_password})")