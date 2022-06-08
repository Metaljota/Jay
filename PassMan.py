
print("WELLCOME TO THE PASSWORD MANAGER APPLICATION")
print("Please select one of the following options")

def write_credentials():#This function will open/create the text file and save the credentials on it.
    text = open("credentials.txt", "a")
    text.write("\n")
    text.write("Website Url: " + input("Url: ") + ("\n"))
    text.write("User Name: " + input("User Name: ") + ("\n"))
    text.write("Password: " + input("password: ") + ("\n"))
    text.close()

def open_credentials(): #This function will open the text file a read it
    text = open("credentials.txt", "r")
    print(text.read())
    text.close() 

choice = ""

while choice != "q":
    print("Select [1] to save credentials")
    print("Select [2] to open saved credentials")
    print("Select [q] to exit")
    choice = input("select your choice: ") #the loop estop here waiting for the user input.
    if choice == "1":
        write_credentials()#this call the function for writing credentials on the file
        print("\nNew credentials has been stored!\n")
    elif choice == "2":
        open_credentials()#this call the function to read the file
    elif choice == "q":
        print("see you next time!")
    else:
        print("\nwrong option, please select again\n")
       
    