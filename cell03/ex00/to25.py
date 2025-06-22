#!/usr/bin/python3

num = int(input("Enter a number less than 25: "))

while num >= 25:
    print("Error")
    num = int(input("Enter a number less than 25: "))

while num <= 25:
        print("Inside the loop, my variable is", num)
        num += 1