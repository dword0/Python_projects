#PASSWORD GENERATOR

import random

print("PASSWORD GENERATOR")
print("==================")
chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()_.,?0123456789'
number = int(input("Number of passwords to be generated : "))
length = int(input("Password Length : "))
print("Here are your passwords : ")
for pwd in range(number):
    passwords = ''
    for c in range(length):
        passwords += random.choice(chars)
    print(passwords)
