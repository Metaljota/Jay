print("WELLCOME TO THE PASSWORD MANAGER APLICATION FOR DIGICORE USERS")

def main_menu():
    print("Enter [1] to create new credentials")
    print("Enter [2] to retreive credentials")
    print("Enter [q] to exit")
    return input("select option: ")


def selected_options(choice):
    if choice == '1':
        credentials = open("credentials.txt", "a") 
        credentials.write("url: " + input("Url: ") + "\n")
        credentials.write("Username: " + input("Username: ") + "\n")
        credentials.write("password: " + input("password: ") + "\n")
        credentials.write("" + "\n")
        credentials.close()
        print("credentials has been stored!")

    elif choice == '2':
        print("" + "\n")
        credentials = open("credentials.txt", "r") 
        print(credentials.read())  		
        credentials.close()

    elif choice == 'q':
        print("\n""See you next time""\n") 

    else:
        print("\n invalid option. Try again please\n")
        selected_options(main_menu())


selected_options(main_menu())
















# new_credentials = (input("Do you want to store new credentials? '1' for yes '2' for no: "))
# new_credentials = 1 or 2
# if new_credentials == 1:
#     continue
# show_credentials = (input("Do you want to load preview credentials?(y/n): "))