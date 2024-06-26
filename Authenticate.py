from db import connect_db

from mysql.connector import Error
from datetime import datetime,timedelta


class ageCalculator:
    def calculate_age(self,birthdate):
        birthdate = datetime.strptime(birthdate, "%Y-%m-%d")

        today = datetime.today()
        age = today.year - birthdate.year - ((today.month, today.day) < (birthdate.month, birthdate.day))
        return age

    def is_greater(self,birthdate,threshold_age):

        age = self.calculate_age(birthdate)
        return age > threshold_age

    

class Authentication:
    def registerUser(self,username,password,role="USER"):
        try:
            conn = connect_db()
            cur = conn.cursor()
            cur.execute('INSERT INTO users (username,password) values(%s,%s)',(username,password))
            conn.commit()
            cur.execute('SELECT id from users where username = %(username)s',{"username":username})
            res = cur.fetchall()
            print(f"Your user id is - {res[0][0]}")
            conn.close()
        except Error as e:
            print(f'Something went Wrong!: {e}')

    def loginUser(self,username,password):
        try:
            conn = connect_db()
            cur = conn.cursor()
            cur.execute('SELECT * FROM users WHERE username = %s AND password = %s', (username, password))

            user = cur.fetchall()
            conn.close()

            if(user):
                print('Login Successful!')
                return True
            else:
                print('Invalid Credentials')
                return False
        except Error as e:
            print(f'Something went wrong!: {e}')

    def loginAdmin(self,adminId,password):
        try:
            conn = connect_db()
            cur = conn.cursor()
            cur.execute('SELECT * FROM admin WHERE adminID = %s AND password = %s', (adminId, password))

            admin = cur.fetchall()
            conn.close()

            if(admin):
                print("Admin Login Successful!")
                return True
            else:
                print("Invalid Credentials!")
                return False

        except Error as e:
            print(f"Invalid Credentials: {e}")


class VehicleRegistration:
    def __init__(self, prefix):
        self.prefix = prefix
        self.current_number = 0

    def generate_registration_number(self):
        self.current_number += 1
        return f"{self.prefix}{self.current_number:06d}"



class viewData:
    def viewVehicles(self, regisNo):
        try:
            conn = connect_db()
            cur = conn.cursor()

            query = 'select * from vehicle_registrations where registration_number = %(registration_number)s'
            cur.execute(query,{'registration_number':regisNo})
            res = cur.fetchall()

            for row in res:
                print(row)
        except Error as e:
            print(f"Cannot fetch records!: {e}")
    
    def viewChallan(self,regisNo):
        try:
            conn = connect_db()
            cur = conn.cursor()

            query = 'select * from chalaans where vehicle_number = %(vehicle_number)s'
            cur.execute(query,{'vehicle_number':regisNo})
            res = cur.fetchall()

            for row in res:
                print(row)
            
        except Error as e:
            print(f"No challan Data found!: {e}")

#bgrp,add,uid, name,
class User:
    def apply_for_registration(self, user_id, purchase_date, engine_number, chassis_number, owner_name,adhar):
        try:
            conn = connect_db()
            cur = conn.cursor()
            query = 'insert into vehicle_registrations (user_id,purchase_date,engine_number,chassis_number,owner_name,aadhar_card) values(%s,%s,%s,%s,%s,%s)'
            cur.execute(query,(user_id,purchase_date, engine_number, chassis_number, owner_name,adhar))
            conn.commit()
            print('Applied for registration succesfully!')
            conn.close()
        except Error as e:
            print(f"user registration failed!:{e}")

    def apply_for_license(self,name,dob,bgrp,add,uid,adhar):
        try:
            conn = connect_db()
            cur = conn.cursor()

            # Issue Need to resolved----------

            # cur.execute('select license_number from driving_licenses where user_id=%(user_id)s',{'user_id':uid})
            # res = cur.fetchone()
            # for lno in res:
            #     print(lno)
            #     if lno is None:
            #         print("Already Owns a License")
            #         return
                # if lno is no:
                #     print(f"Chalaan with this id {chalaan_id} is Already Paid!")
                    # return

            ageObj = ageCalculator()
            res = ageObj.is_greater(dob,18)
            if res is False:
                print("License cannot be issued for Minors!")
                return
            
            age = ageObj.is_greater(dob,75)
            if age is True:
                print("Age Limit Exceeded!")

            query = 'insert into driving_licenses (name,date_of_birth,blood_group,address,user_id,aadhar_card) values(%s,%s,%s,%s,%s,%s)'
            cur.execute(query,(name,dob,bgrp,add,uid,adhar))
            conn.commit()
            print(f"License for user with user id {uid} applied successfully!")
            conn.close()

        except Error as e:
            print(f"Error: {e}")

    def changeOwner(self, regisNo, newOwner, newadhar):
        try:
            conn = connect_db()
            cur = conn.cursor()
            objView = viewData()
            objView.viewVehicles(regisNo)

            query = 'update vehicle_registrations set owner_name = %s,aadhar_card = %s where registration_number = %s'
            cur.execute(query,(newOwner,newadhar,regisNo))
            conn.commit()

            objView.viewVehicles(regisNo)

            print("Owner Changed Successfully!")
            conn.close()

        except Error as e:
            print(f"Owner not changed!: {e}")

    def pay_chalaan(self,regisNo):
        try:
            conn = connect_db()
            cur = conn.cursor()

            objChalaan = viewData()
            objChalaan.viewChallan(regisNo)

            chalaan_id = int(input('Enter the Chalaan ID of the Chalaan to be PAID: '))

            cur.execute('select is_paid from chalaans where id=%(id)s',{'id':chalaan_id})
            res = cur.fetchone()
            for chalaan in res:

                if chalaan == 1:
                    print(f"Chalaan with this id {chalaan_id} is Already Paid!")
                    return
            
            query2 = 'update chalaans set is_paid=%s where id=%s'
            cur.execute(query2,(True,chalaan_id))
            conn.commit()

            print(f"Challan with ID {chalaan_id} PAID successfully!")
            conn.close()
        except Error as e:
            print(f"Chalaan NOT PAID: {e}")
    
    def apply_for_scrapping(self,regisNo):
        conn = connect_db()
        cur = conn.cursor()

        query = 'select * from vehicle_registrations where registration_number = %(registration_number)s'
        cur.execute(query,{'registration_number':regisNo})

        res = cur.fetchone()

        purchaseDate = res[1]
        engineNo = res[2]
        chassisNo = res[3]
        ownerName = res[4]
        regDate = res[6]
        expiryDate = res[7]
        user_id = res[8]


        cur.execute('insert into scrapped_vehicle (purchase_date,engine_number,chassis_number,owner_name,registration_number,registration_date,expiry_date,user_id) values(%s,%s,%s,%s,%s,%s,%s,%s)',(purchaseDate,engineNo,chassisNo,ownerName,regisNo,regDate,expiryDate,user_id))

        conn.commit()

        print(f"Applied for Scrapping of Vehicle {regisNo} successfully!")
        conn.close()

        # print(purchaseDate,engineNo,chassisNo,ownerName,regNo,regDate,expiryDate,user_id)
objLicense = VehicleRegistration("LMH")
objRegist = VehicleRegistration("MH")
class Admin:
    def viewPendingRegistration(self):
        try:
            conn = connect_db()
            cur = conn.cursor()
            query = 'select * from vehicle_registrations where registration_number is NULL'
            cur.execute(query)
            res = cur.fetchall()

            for row in res:
                print(row)
            
            conn.commit()
            conn.close()
        except Error as e:
            print(f"No Pending Request!: {e}")

    def generate_registration_number(self,user_id):
        try:
            conn = connect_db()
            cur = conn.cursor()

            # obj = VehicleRegistration(prefix="MH")
            registration_number = objRegist.generate_registration_number()
            print(registration_number)
            registration_date = datetime.now().date()
            expiry_date = registration_date + timedelta(days=15*365)

            query = 'update vehicle_registrations set registration_number = %s, registration_date=%s, expiry_date=%s where user_id=%s'

            cur.execute(query,(registration_number,registration_date,expiry_date,user_id))
            conn.commit()

            query = 'select * from vehicle_registrations where user_id=%(user_id)s'
            cur.execute(query,{"user_id":user_id})
            res = cur.fetchall()

            for row in res:
                print(row)

        except Error as e:
            print(f"Unable to update Record!: {e}")


    def viewPendingLicenses(self):
        try:
            conn = connect_db()
            cur = conn.cursor()
            query = 'select * from driving_licenses where license_number is NULL'
            cur.execute(query)
            res = cur.fetchall()

            for row in res:
                print(row)
            
            # conn.commit()
            conn.close()
        except Error as e:
            print(f"No Pending Request!: {e}")
    
    def approve_licenses(self,userId):
        try:
            conn = connect_db()
            cur = conn.cursor()

            # obj = VehicleRegistration(prefix="LMH")
            license_number = objLicense.generate_registration_number()
            print(license_number)
            issue_date = datetime.now().date()
            expiry_date = issue_date + timedelta(days=20*365)

            query = 'update driving_licenses set license_number = %s, issue_date=%s, expiry_date=%s, is_approved=%s where user_id=%s'

            cur.execute(query,(license_number,issue_date,expiry_date,True,userId))
            conn.commit()

            query = 'select * from driving_licenses where user_id=%(user_id)s'
            cur.execute(query,{'user_id':userId})
            res = cur.fetchall()

            for row in res:
                print(row)

        except Error as e:
            print(f"Unable to update Record!: {e}")

    def generate_challan(self, regisNo,amount):
        try:
            conn = connect_db()
            cur = conn.cursor()

            query = 'insert into chalaans (vehicle_number,amount) values(%s,%s)'
            cur.execute(query,(regisNo,amount))
            conn.commit()

            objChalaan = viewData()
            objChalaan.viewChallan(regisNo)
            conn.close()
        except Error as e:
            print("Unable to generate chalaan: {e}")

    def view_pending_scrapping(self):
        try:
            conn = connect_db()
            cur = conn.cursor()
            query = 'select * from scrapped_vehicle where is_scrapped is False'
            cur.execute(query)
            res = cur.fetchall()

            for row in res:
                print(row)
            
            # conn.commit()
            conn.close()
        except Error as e:
            print(f"No Pending Request!: {e}")

    def approve_scrapping(self,regisNo):
        try:
            conn = connect_db()
            cur = conn.cursor()

            query = 'update scrapped_vehicle set is_scrapped = True where registration_number=%(registration_number)s'

            cur.execute(query,{'registration_number':regisNo})
            conn.commit()
            query = 'DELETE FROM chalaans WHERE vehicle_number = %(vehicle_number)s'
            cur.execute(query,{'vehicle_number':regisNo})
            conn.commit()
            
            query = 'DELETE FROM vehicle_registrations WHERE registration_number = %(registration_number)s'
            cur.execute(query,{'registration_number':regisNo})
            conn.commit()

        except Error as e:
            print(f"Unable to update Record!: {e}")

# obj = Authenticate()
# obj.loginUser("rohi","rohit1234")

# objage = ageCalculator()
# print(objage.is_greater_than_18("2001-12-12",25))

objUser = User()
# objUser.apply_for_license("Rohit KUmar","2001-12-15","B+","MUNDHWA","1001","123456789123")
# objUser.apply_for_scrapping("MH000001")

objAdmin = Admin()
# objAdmin.approve_scrapping("MH000001")
# objAdmin.viewPendingLicenses()
# objAdmin.approve_licenses("1001")


# obj=Vehicle()
# obj.viewPendingRegistration()
# obj.generate_registration_number("1001")
# obj.pay_chalaan("MH000001")
# obj.generate_challan("MH000001",500.45)
# obj.changeOwner("MH000001","Arpit Singh","234567890123")
# obj1 = viewData()
# obj1.viewVehicles("MH000001")
# obj.apply_for_registration(1001,"2020-12-12","1234","4567","Rohit Kumar","123456789123")