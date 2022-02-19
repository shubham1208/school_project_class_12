# school project hotel management
from contextlib import AbstractAsyncContextManager
from re import A
import keyboard
import mysql.connector as cnt
import tabulate

mdb = cnt.connect(host="localhost", user="root", passwd= "245689731", database="paradise")

csr = mdb.cursor()
# csr.execute("create table customerdetails(SLNO int PRIMARY KEY AUTO_INCREMENT, NAME varchar(50), CHECKIN varchar(20), SUITE varchar(10), ROOMNUM smallint unsigned)")
# csr.execute("create table bookingdetails(NAME varchar(50), DATE_OF_CHECKIN varchar(20), SUITE varchar(10), NUM_OF_DAYS_BOOKED int)")
# csr.execute("create table roomrent(SLNO int PRIMARY KEY AUTO_INCREMENT, SUITE varchar(10), BILL int)")
# csr.execute("create table resturantbill(SLNO int PRIMARY KEY AUTO_INCREMENT, NAME varchar(50), CUISINE varchar(50), QUANTITY int, BILL int)")
# csr.execute("create table gamebill(SLNO int PRIMARY KEY AUTO_INCREMENT, NAME varchar(50), NAME_OF_GAME varchar(50), HOURS int, BILL int)")
# csr.execute("create table fashionbill(SLNO int PRIMARY KEY AUTO_INCREMENT, NAME varchar(50), PRODUCT varchar(50), SIZE varchar(10), BILL int)")



def intro_screen():
    print(""" 

*****************************************************************************************************
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
    

def menu1():
    n = input("Add new entry?(Y/N): ")
    if n.lower() == "y":
        while True:
            a = input("Enter name of customer: ")
            b = input("Enter time of check in (hour, minute rounded up to 30): ")
            c = input("Enter selected suite: ")
            d = input("Enter room number: ")
            csr.execute("insert into customerdetails (NAME, CHECKIN ,SUITE, ROOMNUM) values(%s,%s,%s,%s)", (a,b,c,d))
            mdb.commit()
            menu()
            inp()
            break
    if n.lower() == "n":
        menu()
    if keyboard.is_pressed("Esc"):
        menu()
        inp()
    

    

def menu2():
    n = input("Add new entry?(Y/N): ")
    if n.lower() == "y":
        while True:
            a = input("Enter name of customer: ")
            b = input("Enter date and time of check in: ")
            c = input("Enter selected suite: ")
            d = int(input("Enter number of days booked: "))
            csr.execute("insert into bookingdetails(NAME, DATE_OF_CHECKIN ,SUITE, NUM_OF_DAYS_BOOKED) values(%s,%s,%s,%s)", (a,b,c,d))
            mdb.commit()
            inp()
            break

    if n.lower() == "n":
        csr.execute("select * from bookingdetails")
        a= csr.fetchall()
        print(tabulate.tabulate(a, headers = ['NAME', 'DATE_OF_CHECKIN', 'SUITE', 'NUM_OF_DAYS_BOOKED'], tablefmt='psql'))
    if keyboard.is_pressed("Esc"):
        menu()
        inp()
        
def menu3():
    n = input("Add new entry?(Y/N): ")
    if n.lower() == "y":
        while True:
            a = input("Enter suite: ")
            b = int(input("Enter amount of rent: "))
            csr.execute("insert into roomrent(SUITE, BILL) values(%s,%s)", (a,b))
            mdb.commit()
            menu()
            inp()
            break
    if n.lower() == "n":
        csr.execute("select * from roomrent")
        a= csr.fetchall()
        print(tabulate.tabulate(a, headers = ['SLNO','NAME', 'BILL'], tablefmt='psql'))
    if keyboard.is_pressed("Esc"):
        menu()
        inp()

def menu4():
    n = input("Add new entry?(Y/N): ")
    if n.lower() == "y":
        while True:
            a = input("Enter name of customer: ")
            b = input("Enter quisine: ")
            c = int(input("Enter quantity: "))
            d = int(input("Enter final bill: "))
            csr.execute("insert into resturantbill(NAME, QUISINE, QUANTITY, BILL) values(%s,%s,%s,%s)", (a,b,c,d))
            mdb.commit()
            menu()
            inp()
            break
    if n.lower() == "n":
        csr.execute("select * from resturantbill")
        a= csr.fetchall()
        print(tabulate.tabulate(a, headers = ['SLNO','NAME', 'QUISINE', 'QUANTITY', 'BILL'], tablefmt='psql'))
    if keyboard.is_pressed("Esc"):
        menu()
        inp()
    
    
def menu5():
    n = input("Add new bill?(Y/N): ")
    if n.lower() == "y":
        while True:
            a = input("Enter name of customer: ")
            b = input("Enter type of game played: ")
            c = int(input("Enter hours played(rounded up): "))
            d = int(input("Enter final bill: "))
            csr.execute("insert into gamebill(NAME, NAME_OF_GAME , HOURS, BILL) values(%s,%s,%s,%s)", (a,b,c,d))
            mdb.commit()
            menu()
            inp()
            break
    if n.lower() == "n":
        csr.execute("select * from gamebill")
        a= csr.fetchall()
        print(tabulate.tabulate(a, headers = ['SLNO','NAME', 'NAME_OF_GAME', 'HOURS', 'BILL'], tablefmt='psql'))
    if keyboard.is_pressed("Esc"):
        menu()
        inp()

        
def menu6():
    n = input("Add new bill?(Y/N): ")
    if n.lower() == "y":
        while True:
            a = input("Enter name of customer: ")
            b = input("Enter type of game played: ")
            c = int(input("Enter hours played(rounded up): "))
            d = int(input("Enter final bill: "))
            csr.execute("insert into fashionbill (NAME, PRODUCT , SIZE, BILL) values(%s,%s,%s,%s)", (a,b,c,d))
            mdb.commit()
            menu()
            inp()
            break    
    if n.lower() == "n":
        csr.execute("select * from fashionbill")
        a= csr.fetchall()
        print(tabulate.tabulate(a, headers = ['SLNO','NAME', 'PRODUCT', 'SIZE', 'BILL'], tablefmt='psql'))
    if keyboard.is_pressed("Esc"):
        menu()


def menu7():
    csr.execute("select * from customerdetails")
    a= csr.fetchall()
    print(tabulate.tabulate(a, headers = ['SLNO','NAME', 'CHECKIN', 'SUITE', 'CHECKOUT'], tablefmt='psql'))
    mdb.commit()
    menu()
    inp() 

def menu8():
    name = int(input("Enter SLNO of customer: "))
    csr.execute("SELECT BILL from roomrent where SLNO = {}".format(name))
    a = csr.fetchall()
    csr.execute("SELECT BILL from resturantbill where SLNO = {}".format(name))
    b = csr.fetchall()
    csr.execute("SELECT BILL from gamebill where SLNO = {}".format(name))
    c = csr.fetchall()
    csr.execute("SELECT BILL from fashionbill where SLNO = {}".format(name))
    d = csr.fetchall()
    e = [a,b,c,d,]
    print(tabulate.tabulate(e, headers = ['BILL'], tablefmt='psql'))


def inp():
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
    if inp == 9:
        exit()

intro_screen()
while True:
    try:
        if keyboard.is_pressed('y'):
            menu()
            inp()
            break
    except:
        break
# Shubham Sahu
# Shreyansh Kumar
# Sayan halder
# Simba