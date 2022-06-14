
print("WELLCOME TO THE PASSWORD MANAGER APPLICATION")
print("\nPlease select one of the following options")

def write_credentials():#This function will open/create the text file and save the credentials in it.
    text = open("credentials.txt", "a")
    text.write("\n")
    text.write("Website Url: " + (input("Url: ")) + ("\n"))  
    text.write("User Name: " + (input("User Name: ")) + ("\n"))
    text.write("Password: " + (input("password: ")) + ("\n"))
    text.close()

def display_credentials(): #This function will open the text file a read it
    try:
        text = open("credentials.txt", "r")
        list = text.readlines()
        for item in list:
            credentials = item
            print(credentials, end = "")
            text.close()
    except:
        print("\nThe file does not exist yet\n")


choice = ""

while choice != "q":
    
    print("\nSelect [1] to save credentials")
    print("Select [2] to open saved credentials")
    print("Select [q] to exit")
    
    choice = input("\nselect your choice: ") 
    
    if choice == "1":
        write_credentials()
        print("\nNew credentials has been stored!\n")
    elif choice == "2":
        display_credentials()
    elif choice == "q":
        print("\nsee you next time!\n")
    else:
        print("\nwrong option, please select again\n")
       
    

