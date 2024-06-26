from Authenticate import *
# import getpass

# class User:
#     def register(self):
#         firstName = input("FirstName: ")
#         lastName = input("LastName: ")
#         userId = input("UserID: ")
#         password = input("Password: ")
        
#         obj = Authentication()
#         obj.registerUser(firstName,lastName,userId,password)
    
#     def login(self):
#         userId = input("userID: ")
#         password = input("Password: ")

#         obj = Authentication()
#         obj.loginUser(userId,password)

    

# class Admin:
#     def loginAdmin(self,adminId,password):
#         adminId = input("adminID: ")
#         password = input("Password: ")

#         obj = Authentication()
#         obj.loginAdmin()

# class viewData:
#     def viewVehicle():

#         pass
#     def viewLicense():
#         pass
#     def viewChallan():
#         pass


# def main():
    # print("=========| Welcome, TO RTO |==========")
    # print("+----+----------------+")
    # print("| 1. |  User      |")
    # print("| 2. |  Admin     |")
    # print("+----+----------------+")

#     user_role=input('Enter Options: ')
#     match user_role:
#         case '1':
#             print('User')
#             user = User()
#             user.register()
            
#         case '2':
#             print('Admin')
#         case _:
#             print('Invalid choice')


# if __name__ == "__main__":
#     main()

import getpass
import os

# Sample users and roles data
users = {
    'admin': {'password': 'admin', 'role': 'admin'},
    'bob': {'password': 'qwerty456', 'role': 'user'},
    'charlie': {'password': 'asdfgh789', 'role': 'user'}
}

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def print_header(title):
    clear_screen()
    print("="*50)
    print(f"{title.center(50)}")
    print("="*50)

obj = Authentication()
userObj = User()
userAdmin = Admin()
dataObj = viewData()

def registerUser():
    username = input("Username: ")
    password = input("Password: ")

    obj.registerUser(username,password)

def loginUser():
    username = input("Username: ")
    password = input("password: ")

    x = obj.loginUser(username,password)
    if x is True:
        user_menu()

def user():
    print("1.Login - Already a User")
    print("2.Register - New User")
    print("3.Exit")


    user_data = int(input("Select the option: "))

    match user_data:
        case 1:
            loginUser()

        case 2:
            registerUser()
            user()
        case 3:
            print("Exit")
            return
        case _:
            print("Invalid choice")
            user()


def admin_menu():
    while True:
        print_header("Admin Menu")
        print("1. View Vehicles")
        print("2. View Licenses")
        print("3. View Challans")
        print("4. Approve Vehicle Registration")
        print("5. Approve License")
        print("6. Generate Challan for Users")
        print("7. Apply for Scrap")
        print("8. Logout")
        choice = input("\nEnter your choice: ")
        
        match choice:
            case '1':
                view_vehicles()
            case '2':
                view_licenses()
            case '3':
                view_challans()
            case '4':
                approve_vehicle_registration()
            case '5':
                approve_license()
            case '6':
                generate_challan()

            case '7':
                approve_scrap()
            case '8':
                main()
            case _:
                print("Invalid choice. Please try again.")
        input("\nPress Enter to continue...")

def user_menu():
    while True:
        print_header("User Menu")
        print("1. Apply Vehicle Registration")
        print("2. Apply License")
        print("3. Change Owner")
        print("4. View Vehicle")
        print("5. View License")
        print("6. View Challan")
        print("7. Apply for Scrap")
        print("8. Logout")
        choice = input("\nEnter your choice: ")
        
        match choice:
            case '1':
                apply_vehicle_registration()
            case '2':
                apply_license()
            case '3':
                change_owner()
            case '4':
                view_vehicles()
            case '5':
                view_licenses()
            case '6':
                view_challans()
            case '7':
                apply_scrap()
            case '8':
                main()
            case _:
                print("Invalid choice. Please try again.")
        input("\nPress Enter to continue...")

# Placeholder functions for each option
def view_vehicles():
    regisNo = input("Registration Number: ")
    dataObj.viewVehicles(regisNo)

def view_licenses():
    pass

def view_challans():
    regiNo = input("Registration Number: ")
    objUser.pay_chalaan(regiNo)

def approve_vehicle_registration():
    user_id = input("User_ID: ")
    objAdmin.generate_registration_number(user_id)

def approve_license():
    user_id = input("User_ID: ")
    objAdmin.approve_licenses(user_id)

def generate_challan():
    regisNo = input("Registration Number: ")
    amount = input('Amount: ')

    objAdmin.generate_challan(regisNo,amount)

def apply_scrap():
    regiNo = input("Registration Number: ")
    userObj.apply_for_scrapping(regiNo)

def approve_scrap():
    objAdmin.view_pending_scrapping()
    regisNo = input("Registration Number: ")
    objAdmin.approve_scrapping(regisNo)

def apply_vehicle_registration():
    userId = input("UserID: ")
    purdate = input("Purchase Date (yyyy-mm-dd): ")
    egnNo = input("Engine Number: ")
    chsNo = input("Chassis Number: ")
    own = input("Owner Name: ")
    adhCard = input("Aadhar Card: ")

    objUser.apply_for_registration(userId,purdate,egnNo,chsNo,own,adhCard)

def apply_license():
    name = input('Name:')
    dob = input("Date of Birth (yyyy-mm-dd): ")
    bgrp = input("Blood Group: ")
    addr = input("Adress: ")
    uid = input("UserId: ")
    adhar = input("Aadhar Card: ")

    objUser.apply_for_license(name,dob,bgrp,addr,uid,adhar)

def change_owner():
    regisNo = input("Registration Number: ")
    newOwner = input("New User: ")
    newAdhar = input("Aadhar of New User: ")

    objUser.changeOwner(regisNo,newOwner,newAdhar)

# def view_vehicle():
#     print_header("View Vehicle")
#     print("Viewing vehicle...")

# def view_license():
#     print_header("View License")
#     print("Viewing license...")

# def view_challan():
#     print_header("View Challan")
#     print("Viewing challan...")

# def login():
#     clear_screen()
#     print_header("CLI Login Portal")
#     username = input("Username: ")
#     password = getpass.getpass("Password: ")
    
#     if username in users and users[username]['password'] == password:
#         print(f"\nWelcome, {username}!")
#         input("\nPress Enter to continue...")
#         role = users[username]['role']
#         if role == 'admin':
#             admin_menu()
#         elif role == 'user':
#             user_menu()
#     else:
#         print("\nInvalid username or password. Please try again.")
#         input("\nPress Enter to continue...")

def main():
    print("=========| Welcome, TO RTO |==========")
    print("+----+----------------+")
    print("| 1. |  User      |")
    print("| 2. |  Admin     |")
    print("+----+----------------+")

    user_input = int(input("Enter the option: "))

    match user_input:
        case 1: 
            user()
        case 2:
            adminId = input("adminID: ")
            password = input("Password: ")

            x=obj.loginAdmin(adminId,password)
            if x is True:
                admin_menu()
        case _:
            print("Invalid choice")

    # attempts = 3
    # while attempts > 0:
    #     # login()
    #     attempts -= 1
    #     if attempts > 0:
    #         retry = input("\nDo you want to try again? (y/n): ").strip().lower()
    #         if retry != 'y':
    #             break
    #     else:
    #         print("Too many failed attempts. Exiting.")
    #         break

if __name__ == "__main__":
    main()
