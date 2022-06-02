#create a syntactically correct 'if' block and run it to prove it works
#Remove the indent and run the script to see the syntax error

# if 7 > 3:
#  print ("seven is greater than three")
# # comment
# # Comment
# # comment 

# z = "SEPARATION"
# print (z)

# #create a variable x, assign it an integer value and print it out
# #create two variables using snake case (call them whatever you want)
# #assign an integer to one variable, assign a text string to the other Variable
# x = 0
# the_value_of_seven = 7
# AnotherValueInput = "text"
# print (x)
# print (AnotherValueInput)

# z = "SEPARATION"
# print (z)
# #create a variable and display the variable and some text in a single print() method
# x = 23
# print ("x is equal to", x)


# z = "SEPARATION"
# print (z)
# # Variables store data of different types
# # x = "Hello world" 				– a string
# # x = 20 						– an integer
# # X = 2.3						- a float
# # x = ["virus", "worm", "Trojan"] 		– a list
# # x = {"name" : "Renu", "age" : 42} 	– a dictionary
# # examples..... 
# y = 40
# t = 2.3 
# d = {"travel": "car", "other": "flight"}
# print (type(y))
# print (type(t))
# print (type (d))
# #task
# # create a integer variable and print its type()
# # create a list, populate it with an integer, float and string, and print the list
# # create a dictionary with two keys and related values, and print it
# a = 50 
# print (type(a))
# b = ["some numbers", "20", "5.5"]
# print (type(b))
# c = {"value1" : "blue", "value2" : "white"}
# print (type(c))

# z = "SEPARATION"
# print (z)
# # Variables of one type can be changed into another type. This is known as 'casting'. 
# x = 2.2 
# print (int(x))

# z = "SEPARATION"
# print (z)
#create a float variable equal to 3.35. Cast it into an int and notice the round down.
#create a string variable equal to "myString". Attempt to cast it to an integer 
# and notice the error#create a string variable equal to "2". Cast it to an integer
# f = 3.35 
# print (int(f))
# g = "mystring"
# print (int(g))
# h = "2"
# print (int(h))


# z = "SEPARATION"
# print (z)
# mydata = input("write something here: ")
# print (mydata) 

# t = 4
# t = "sally" 
# print (t)

#                                      CLASS 27 MAY 2022

# mystring = "hello world!!"
# print(mystring[0]) print the first index
# print(mystring[2:5]) print the second index until 5
# print(mystring[:5]) print from the begining until 5
# print(mystring[2:]) print from the second until the end

# print(mystring.upper()) print everything in upper case

#methods examples. replace, split, etc.... we can find the methods list here:
# https://www.w3schools.com/python/python_ref_string.asp
# https://www.w3schools.com/python/python_strings_methods.asp 

# mystring = "hello world!!"
# print(mystring.replace("h","j"))

# mystring = "hello"
# mystring2 = "world"
# print(mystring + " " + mystring2) #the espace "" create the space in the result. 

# x = 2
# y = 3
# print ("x is equal to {1} and y is equal to {0}" .format(x,y))

#ESCAPE CHARACTERS
# print ("display \n a \n double \n quote") #these are scape list

#create a string and display only the 3rd to 6th characters using slicing
# mystring = "hello world!!"
# print(mystring[3:7])
# print(mystring[3], mystring[7]) This one print only the indexs selected

#create a string, whose words are separated by a dot (.) and split that string into a list with . 
# being the separator.use split('.')
# string = "take.the.hammer"
# print(string.split('.')) 

#create two strings, concatenate with two white spaces in between and display
# string1 = "rock and roll"
# string2 = "heavy metal"
# print(string1 + " " + string2)

#use one method from string methods and give it a try. The team used COUNT method. 
# txt = "this is a sampple version of a text that could be long or not"
# print(txt.count("o")) 

#BOOLEANS, operators
#print(1 + 2 * 3) #this one start from 3*2 and then +1
#print((1 + 2) * 3) #this one start from 1+2 and then *3 
#print(9/2)
#print(9%2) #this one shows what remains after the division.  

#an example how to use %
# x = int(input("enter a number: "))
# if (x % 2) == 0:
#     print("number is even")
# else:
#     print("number is odd")

#print(9//2) #with double / we roundup the final number

#Use two Arithmetic operators to add two numbers toguether, multiplay by 4 and 
# find the reminder after divide by 3. 
#print(((3 + 4)*4)%3)
 
#LISTS
#https://www.w3schools.com/python/python_lists_methods.asp

# mylist = ["apple", "banana", "cherry"]
#print(mylist) #shows the hole thing 
#print(mylist[2]) #it shows "cherry"

# mylist[0:2] = ["coco", "apricot"] #change the especific index 
# print(mylist)

#Create a list and print it
# thelist = ["red", "blue", "green", "yellow", "white"]
# print(thelist) 

#Use count() and display the number of items of a particular value in the list
# thelist = ["red", "blue", "green", "yellow", "white"]
# print(thelist.count("blue"))

#write a script that takes in a string as input from a user and uses count() 
# to count how many times the letter 'e' occurs in the string. Print out the string, 
# and the number of times the letter 'e' occurs.
x = str(input("write some words: "))
print(x)
print(x.count("e"))

