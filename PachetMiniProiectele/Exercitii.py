"""" 1.Create a program that asks the user to enter their name and their age. Print out a message addressed to them that tells them the year that
they will turn 100 years old. Note: for this exercise, the expectation is that you explicitly write
out the year (and therefore be out of date the next year)"""

# name = input("Please tell us your name:")
# age = int(input("Please tell us you age:"))
#
# print("Your name is" + name)
#
# if age <= 100:
#     current_year = 2024
#     dif = 100 - age
#     oldie = current_year - age + 100
#     print("Your age is " + str(age))
#     print("You will turn 100 in " + str(dif) + " years")
#     print("Also, when you turn 100 years old, it will be the year " + str(oldie))
# else:
#     print("You're a dinosaur!!! Go to sleep!")

"""" 2.Ask the user for a number. Depending on whether the number is even or odd, print out an appropriate message 
to the user. If the number is a multiple of 4, print out a different message.
Ask the user for two numbers: one number to check (call it num) and one number to divide by (check). 
If check divides evenly into num, tell that to the user. If not, print a different appropriate message."""

# num = int(input("Tell me a number:"))
# check = int(input("Tell me a number to divide the first one:"))
#
# if num % 4 == 0:
#     print("The number is  multiple of 4.")
#
# if num % 2 == 0:
#     print("The number you printed first is " + str(num) + " and is even.")
# else:
#     print("The number you printed first is " + str(num) + " and is odd.")
#
# if num % check == 0:
#     print("The first number " + str(num) + " is devided by the second number " + str(check) + ".")
# else:
#     print("The number " + str(num) + " does not divide evenly by " + str(check) + ".")

"""" 3.Take a list, say for example this one:
  a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89] and write a program that prints out all the elements of the list that are less than 5.

-> Instead of printing the elements one by one, make a new list that has all the elements less than 5 from this list 
in it and print out this new list.
-> Write this in one line of Python.
-> Ask the user for a number and return a list that contains only elements from the original list a that are smaller than 
that number given by the user."""

# a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
# b=[]
# for i in a:
#     if i<5:
#         b.append(i)
# print(b)

# b=[i for i in a if i<5]
# print (b)

# num=input("Tell me a number:")
# c=[j for j in a if j < int(num)]
# print(c)

"""" 4. Create a program that asks the user for a number and then prints out a list of all the divisors of that number. 
(If you don’t know what a divisor is, it is a number that divides evenly into another number."""

# num = int(input ("Print a number:"))
# d = 1
# list_divizori=[]
#
# for d in range(1, num+1):
#     if num % d ==0:
#         list_divizori.append(d)
#         d+=1
# print(list_divizori)

""" 5. Take two lists, say for example these two:
  a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
  b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
and write a program that returns a list that contains only the elements that are common between the lists 
(without duplicates). Make sure your program works on two lists of different sizes.

Extras:
Randomly generate two lists to test this
Write this in one line of Python (don’t worry if you can’t figure this out at this point - we’ll get to it soon)"""

# a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
# b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
# c=a+b
# print(set(c))

# list_A = list(map(int, input("Create a random list of numbers (separate by space): ").split(',')))
# list_B = list(map(int, input("Create a 2nd random list of numbers (separate by space): ").split(',')))
# list_C= list_A + list_B
# print(set(list_C))

# https://www.practicepython.org/