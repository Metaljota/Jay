
print("WELLCOME TO THE PASSWORD MANAGER APPLICATION")
print("Please select one of the following options")

def encryption(clearText):
    clearText = "myPassword"
    charSet="0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz`~!@#$%^&*()_-=+|\}]{[\"':;?/>.<, "
    encText = "".join([charSet[(charSet.find(c)+3)%95] for c in clearText])
    return(encText)

def decryption(encText):
    # encText = "myPassword"
    charSet="0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz`~!@#$%^&*()_-=+|\}]{[\"':;?/>.<, "
    clearText = "".join([charSet[(charSet.find(c)-3)%95] for c in encText])
    return(clearText)

def write_credentials():#This function will open/create the text file and save the credentials in it.
    text = open("credentials.txt", "a")
    text.write("\n")
    text.write("Website Url: " + encryption (input("Url: ")) + ("\n"))
    text.write("User Name: " + encryption (input("User Name: ")) + ("\n"))
    text.write("Password: " + encryption (input("password: ")) + ("\n"))
    text.close()

def display_credentials(): #This function will open the text file a read it
    try:
        text = open("credentials.txt", "r")
        print(decryption + text.read())
        text.close()
    except:
        print("\nThe file does not exist yet\n")


choice = ""

while choice != "q":
    
    print("Select [1] to save credentials")
    print("Select [2] to open saved credentials")
    print("Select [q] to exit")
    
    choice = input("select your choice: ") 
    
    if choice == "1":
        write_credentials()
        print("\nNew credentials has been stored!\n")
    elif choice == "2":
        display_credentials()
    elif choice == "q":
        print("\nsee you next time!\n")
    else:
        print("\nwrong option, please select again\n")
       
    

