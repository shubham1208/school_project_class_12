# school project hotel management
import keyboard
def intro_screen():
    print("""
                
             $$$$$$\   $$$$$$\  $$\   $$\ $$\   $$\ $$\  $$$$$$\        $$\   $$\  $$$$$$\  $$$$$$$$\ $$$$$$$$\ $$\       
            $$  __$$\ $$  __$$\ $$ |  $$ |$$ |  $$ |$  |$$  __$$\       $$ |  $$ |$$  __$$\.\__$$  __|$$  _____|$$ |      
            $$ /  \__|$$ /  $$ |$$ |  $$ |$$ |  $$ |\_/ $$ /  \__|      $$ |  $$ |$$ /  $$ |   $$ |   $$ |      $$ |      
            \$$$$$$\  $$$$$$$$ |$$$$$$$$ |$$ |  $$ |    \$$$$$$\        $$$$$$$$ |$$ |  $$ |   $$ |   $$$$$\    $$ |      
             \____$$\ $$  __$$ |$$  __$$ |$$ |  $$ |     \____$$\       $$  __$$ |$$ |  $$ |   $$ |   $$  __|   $$ |      
            $$\   $$ |$$ |  $$ |$$ |  $$ |$$ |  $$ |    $$\   $$ |      $$ |  $$ |$$ |  $$ |   $$ |   $$ |      $$ |      
            \$$$$$$  |$$ |  $$ |$$ |  $$ |\$$$$$$  |    \$$$$$$  |      $$ |  $$ | $$$$$$  |   $$ |   $$$$$$$$\ $$$$$$$$\ 
             \______/ \__|  \__|\__|  \__| \______/      \______/       \__|  \__| \______/    \__|   \________|\________|
                                                PRESS Y TO PROGRESS                                                                          
                
#####################################################################################################################################
    """)
def menu1():
    pass
def menu2():
    pass
def menu3():
    pass
def menu4():
    pass
def menu5():
    pass
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
    if inp == 9:
        menu9()

intro_screen()
while True:
    try:
        if keyboard.is_pressed('y'):
            menu()
            break
    except:
        break
