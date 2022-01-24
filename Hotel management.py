# school project hotel management
import keyboard
from calendar import c
import mysql.connector as cnt
import datetime

mdb = cnt.connect(host="localhost", user="root", passwd= "245689731", database="paradise")

csr = mdb.cursor()
csr.execute("create table customerdetails(SLNO int PRIMARY KEY AUTO_INCREMENT, NAME varchar(50), CHECKIN varchar(20), SUITE varchar(10), ROOMNUM smallint unsigned)")
csr.execute("create table bookingdetails(NAME varchar(50), DATE_OF_CHECKIN varchar(20), SUITE varchar(10), NUM_OF_DAYS_BOOKED int)")
csr.execute("create table roomrent(SLNO int PRIMARY KEY AUTO_INCREMENT, SUITE varchar(10), RENT int")
csr.execute("create table resturantbill(SLNO int PRIMARY KEY AUTO_INCREMENT, NAME varchar(50), CUISINE varchar(50), QUANTITY int, BILL int")
csr.execute("create table gamebill(SLNO int PRIMARY KEY AUTO_INCREMENT, NAME varchar(50), NAME_OF_GAME varchar(50), HOURS int, GAMEBILL int")


def intro_screen():
    print(""" 
             /$$$$$$$   /$$$$$$  /$$$$$$$   /$$$$$$  /$$$$$$$  /$$$$$$  /$$$$$$  /$$$$$$$$
            | $$__  $$ /$$__  $$| $$__  $$ /$$__  $$| $$__  $$|_  $$_/ /$$__  $$| $$_____/
            | $$  \ $$| $$  \ $$| $$  \ $$| $$  \ $$| $$  \ $$  | $$  | $$  \__/| $$      
            | $$$$$$$/| $$$$$$$$| $$$$$$$/| $$$$$$$$| $$  | $$  | $$  |  $$$$$$ | $$$$$   
            | $$____/ | $$__  $$| $$__  $$| $$__  $$| $$  | $$  | $$   \____  $$| $$__/   
            | $$      | $$  | $$| $$  \ $$| $$  | $$| $$  | $$  | $$   /$$  \ $$| $$      
            | $$      | $$  | $$| $$  | $$| $$  | $$| $$$$$$$/ /$$$$$$|  $$$$$$/| $$$$$$$$
            |__/      |__/  |__/|__/  |__/|__/  |__/|_______/ |______/ \______/ |________/

                                       PRESS Y TO CONTINUE                                       
*****************************************************************************************************                                                                              
                                                                              """)
def menu1():
    n = input("Add new entry?(Y/N): ")
    a = input("Enter name of customer: ")
    b = input("Enter time of check in (hour, minute rounded up to 30): ")
    c = input("Enter selected suite: ")
    d = input("Enter room number: ")
    inp = csr.execute("insert into customerdetails (NAME, CHECKIN ,SUITE, ROOMNUM) values(%s,%s,%s,%s)", (a,b,c,d))

    if n.lower() == "y":
        inp
    if n.lower() == "n":
        pass
    if keyboard.is_pressed("Esc"):
        menu()

def menu2():
    n = input("Add new entry?(Y/N): ")
    a = input("Enter name of customer: ")
    b = input("Enter date and time of check in: ")
    c = input("Enter selected suite: ")
    d = int(input("Enter number of days booked: "))
    inp = csr.execute("insert into customerdetails (NAME, DATE_OF_CHECKIN ,SUITE, NUM_OF_DAYS_BOOKED) values(%s,%s,%s,%s)", (a,b,c,d))
    if n.lower() == "y":
        inp
    if n.lower() == "n":
        pass
    if keyboard.is_pressed("Esc"):
        menu()
        
def menu3():
    n = input("Add new entry?(Y/N): ")
    a = input("Enter suite: ")
    b = input("Enter amount of rent: ")
    inp = csr.execute("insert into roomrent(NAME, RENT) values(%s,%s)", (a,b))
    if n.lower() == "y":
        inp
    if n.lower() == "n":
        pass
    if keyboard.is_pressed("Esc"):
        menu()

def menu4():
    n = input("Add new entry?(Y/N): ")
    a = input("Enter name of customer: ")
    b = input("Enter quisine: ")
    c = int(input("Enter quantity: "))
    d = int(input("Enter final bill: "))
    inp = csr.execute("insert into resturantbill(NAME, QUISINE, QUANTITY, BILL) values(%s,%s,%s,%s)", (a,b,c,d))
    if n.lower() == "y":
        inp
    if n.lower() == "n":
        pass
    if keyboard.is_pressed("Esc"):
        menu()

def menu5():
    a = input("Enter name of customer: ")
    b = input("Enter type of game played: ")
    c = int(input("Enter hours played(rounded up): "))
    d = int(input("Enter final bill: "))
    n = input("Add new bill?(Y/N): ")
    if n.lower() == "y":
        csr.execute("insert into customerdetails (NAME, NAME_OF_GAME , HOURS, GAMEBILL) values(%s,%s,%s,%s)", (a,b,c,d))
    if n.lower() == "n":
        pass
    if keyboard.is_pressed("Esc"):
        menu()

        
def menu6():
    pass
def menu7():
    pass
def menu8():
    pass

def menu9():
    pass

def menu():
    print("""
                    #########################################
                    $        1. CUSTOMER DETAILS            $
                    $                                       $
                    $        2. BOOKING RECORD              $
                    $                                       $
                    $        3. ROOM RENT                   $
                    $                                       $
                    $        4. RESTAURENT BILL             $
                    $                                       $
                    $        5. GAMING BILL                 $
                    $                                       $
                    $        6. FASHION STORE BILL          $
                    $                                       $
                    $        7. DISPLAY CUSTOMER DETAILS    $
                    $                                       $
                    $        8. TOTAL BILL                  $
                    $                                       $
                    $        9. EXIT                        $
                    #########################################
    """, "\n")
    inp = int(input("ENTER MENU NUMBER HERE: "))
    if inp == 1:
        menu1()
    if inp == 2:
        menu2()
    if inp == 3:
        menu3()
    if inp == 4:
        menu4()
    if inp == 5:
        menu5()
    if inp == 6:
        menu6()
    if inp == 7:
        menu7()
    if inp == 8:
        menu8()

intro_screen()
while True:
    try:
        if keyboard.is_pressed('y'):
            menu()
            break
    except:
        break
# Shubham Sahu
# Shreyansh Kumar
# Sayan halder
# Simba