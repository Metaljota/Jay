print("WELLCOME TO THE PASSWORD MANAGER APLICATION FOR DIGICORE USERS")

def print_options():
    
    while choice != 'q':
        print("Enter [1] to create new credentials")
        print("Enter [2] to retreive credentials")
        print("Enter [q] to exit")
        break
    choice = input("select option: ")

choice = ''

print_options()

if choice == '1':
    credentials = open("credentials.txt", "a") 
    credentials.write("url: " + input("Url: ") + "\n")
    credentials.write("Username: " + input("Username: ") + "\n")
    credentials.write("password: " + input("password: ") + "\n")
    credentials.close()
    print("credentials has been stored!")

elif choice == '2':
    credentials = open("credentials.txt", "r") 
    print(credentials.read())  		
    credentials.close()

elif choice == 'q':
    print("See you next time") 

else:
    print_options()














# new_credentials = (input("Do you want to store new credentials? '1' for yes '2' for no: "))
# new_credentials = 1 or 2
# if new_credentials == 1:
#     continue
# show_credentials = (input("Do you want to load preview credentials?(y/n): "))