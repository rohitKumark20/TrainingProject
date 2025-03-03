from Authenticate import *
import os
import getpass

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
    password = getpass.getpass("Password: ")

    obj.registerUser(username,password)

def loginUser():
    username = input("Username: ")
    password = getpass.getpass("password: ")

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
            exit()
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
        print("7. Approve for Scrap")
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
    userId = input("UserID: ")
    dataObj.viewLicenses(userId)

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
            password = getpass.getpass("Password: ")

            x=obj.loginAdmin(adminId,password)
            if x is True:
                admin_menu()
        case _:
            print("Invalid choice")

if __name__ == "__main__":
    main()
