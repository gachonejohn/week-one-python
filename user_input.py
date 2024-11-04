# Write a program that asks the user for their name, age, and location 
# and then prints out a personalized message.

name = input('Whats your name: ')
age = int(input('Enter your age: '))
location = input('Enter your location: ')

print(f"Hi {name}, from {location}. You are {age} years old.")