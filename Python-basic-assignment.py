# Task 1: Variables & Data Types
# Declare variables of different data types: string, integer, float, boolean, list
# Print each variable along with its data type using the type() function

Name = 'Seunfunmi' #string
Age = 12 #integer
Weight = 65.4 #float
is_female = True #boolean
Hobby = {'singing', 'dancing', 'reading'} #list

print(Name, type(Name))
print(Age, type(Age))
print(Weight, type(Weight))
print(is_female, type(is_female))
print(Hobby, type(Hobby))


# Task 2: User Input & Conditional Statements
# Ask the user to input their age
# If age is 18 or above, print "You are eligible to vote."
# If age is below 18, print "You are not eligible to vote."

AgeInput = int(input('Enter Age'))

if AgeInput >= 18:
    print('You are eligible to vote')
else:
    print('You are not eligible to vote')


# Task 3: Loops
# Write a for loop that prints numbers from 1 to 10
# for loop
for x in range(1, 11):
    print(x)
# Write a while loop that prints even numbers between 1 and 20
# while loop
num = 2
while num <= 20:
    print(num)
    num += 2


# Task 4: Mini Challenge
# Create a list of 5 fruits
# Use a loop to print each fruit in uppercase letters
# If the fruit is "banana", skip it using continue
Fruits = ['Banana', 'Mango', 'Apple', 'Orange', 'Watermelon']
for fruit in Fruits:
    if fruit == 'Banana':
        continue
    print(fruit.upper())