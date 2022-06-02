#                                     HOME WORK

#QUESTION FROM SLAK GROUP 
# x = 65549325
# print(len(str(x)))

#TUPLE is set with () and is faster than list. Beside it can not be changed or alterated. 
# atuple = ("apple", "banana", "carrot", "cherry", "apple")
# print(atuple)

#SET is done by {} and it gives you random orders. If there is two similar 
# items it appears only one.
# thisset = {"apple", "banana", "cherry", "apple"}
# print(thisset) 
# print(len(thisset)) #with len we determined how many items are in the set (or any other variable)

#DICTIONARY. Do not allows duplicated. 
# thisdict = {"brand": "Ford", "model": "Mustang", "year": 1964, "year": 2020}
# print(thisdict)

#IF... Else. There is a list of logical conditions: 
# Equals: a == b
# Not Equals: a != b
# Less than: a < b
# Less than or equal to: a <= b
# Greater than: a > b
# Greater than or equal to: a >= b 
#---------
# a = input("number: ")
# b = input("number2: ")
# if b > a:
#  print("b is greater than a")
# elif a == b:
#  print("same")
# else: 
#  print("no way")

#WHILE is used to create a loop. 
# i = 1
# while i < 6:
#   print(i)
#   i += 1 # ESTO SIGNIFICA QUE i = i + 1
#--------------------------
# i = 1
# while i < 6:
#   print(i)
#   if (i == 3):
#     break
#   i += 1
#-------------------------
# i = 1
# while i < 6:
#   print(i)
#   i += 1
# else:
#   print("i is no longer less than 6")

#FOR create a list in vertical 
# fruits = ["apple", "banana", "cherry"]
# for z in fruits:
#     print(z)
#--------------------
# for x in "banana":
#   print(x)
#--------------------
# for x in range(6):
#   print(x) 
#--------------------
# for x in range(6):
#   print(x)
# else:
#   print("Finally finished!")

#FUNCTIONS ................Not quite clear about this one
# def my_function(fname):
#   print(fname + " Jota")
# my_function("Emil")
# my_function("Tobias")
# my_function("Linus")
#--------------------------
# x = 300
# print(x) 
# def myfunc():
#   x = 200
#   print(x)
# myfunc()

#FORMAT
# price = 49
# txt = "The price is {} dollars"
# print(txt.format(price))
# price = 49
# txt = "The price is {:.2f} dollars"
# print(txt.format(price))
# quantity = 3
# itemno = 567
# price = 49
# myorder = "I want {} pieces of item number {} for {:.2f} dollars."
# print(myorder.format(quantity, itemno, price))

#                                          CLASS 1 JUNE 2022

# quantity = 3
# itemno = 4
# price = 5
# myorder = "{2} {0} {1}"
# print(myorder.format(quantity, price, itemno))

# Create a script that takes the integer 3 as input from 
# the user and increments it five times using a while loop and, displays the result
# myNum = int(input("write a number three: "))
# while myNum < 9:
#     myNum += 1
#     print(myNum)
#--------------Other way...
# myNum = int(input("write a number three: "))
# total = 0
# while myNum < 9:
#     myNum += 1
#     total += myNum
#     print(total)

#Include an if statement in the script so that the while loop exits 
# when the integer is equal to 5
# myNum = int(input("write a number three: "))
# while myNum < 10:
#     myNum += 1
#     print(myNum)
#     if myNum == 5:
#      break 

#Create a for loop that iterates through and prints each letter of the string "myString"
# for everyElement in "mystring":
#     print(everyElement) #we can use ,end=" " after everyElement to make it horizontaly.

#Add code so that the letter S is not displayed
# for everyElement in "myString":
#     if everyElement == "S":
#       continue
#     print(everyElement)

#create a script that iterates through a for loop five times. 
# Each time through the loop the numbers 2 through to 6 should be displayed. 
# Use the range() method control the number of repetitions
# for x in range(2,7):
#     print(x) #not complete

#FUNCTIONS
#Create a function that accepts a single argument and displays it. 
# Call it from the body of the code
# def my_function(name):
#   print(name)
# my_function("jay")
#----------------------------------------
# Create a script that asks for two numbers inputted from the command line, 
# passes those two numbers as arguments to a function. 
# The function will add the two numbers, and return the result to be printed 
# by the main part of the script.
# def myfunc(x, y):
#     i = x + y
#     return i
# num1 = int(input("enter a number: "))
# num2 = int(input("enter another number: "))
# z = myfunc(num1, num2)
# print(z)
#--------------------------------------
#Create a script with a hard-coded string and use len() to display 
# the number of characters in the string
# y = str("melbourne")
# print(len(y))
#--------------------------------------
#Create a function titled 'dice' that simulates the rolling of two dice. 
# It should be called once, and return two integer values each chosen randomly 
# from a 1 to 6 range
# import random 
# def dice():
#     dice1 = random.randrange(1,6)
#     dice2 = random.randrange(1,6)
#     return dice1, dice2
# print(dice())
#--------------------------------------
#MENU FOR GRETTINGS 
# print("\n This program says hello and goodbye")
# choice = ''
# while choice != 'q':   
#     print("\n[1] Enter 1 to say hello to yourself.")
#     print("[2] Enter 2 to say by to yourself")     
#     choice = input("\nMake your choice ")   
#     if choice == '1':
#         name = input("enter name: ")
#         print("\n hello", name)
#     elif choice == '2':
#         name = input("enter name: ")
#         print("\n goodbye", name)
#     else:
#         print("\nInvalid option, please try again.\n")
# print("Program exit.")
#-------------------------------------------
#MENU TASK
#Create a menu with three options. 1. Add numbers; 2. Subtract numbers. 3. Exit
# If option 1 is chosen a function should be called that asks for input of two numbers, adds them, displays the result and returns to the menu
# If option 2 is chosen a function should be called that asks for input of two numbers, subtracts them, displays the result and returns to the menu
# If option 3 is chosen the program should exit.
# If any other input is entered the menu simply repeats

def add():
    num1 = float(input("enter first number: "))
    num2 = float(input("enter first number: "))
    print(num1 + num2)

print("\n This program do math")
choice = ''
while choice != 'q':
    print("\n[1] Enter 1 to add numbers: ")
    print("\n[2] Enter 2 to subtract numbers: ")
    print("\nEnter q to quit")
    choice = input("\nMake your choice: ")

    if choice == '1':
        add()

    elif choice == '2':
        num1 = int(input("enter the first number: "))
        num2 = int(input("enter the second number: "))
        print(num1 - num2)

    else:
        print("\nInvalid option, please try again. \n")

print("program exit.")








  
    
   

     


