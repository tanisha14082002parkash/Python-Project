#Project on RAILWAY MANAGEMENT SYSTEM
#---------------------------------------------------------------------------------------------
#MODULE: RAILWAYFRONTEND
import RAILWAYMENU
import TRAIN
import TICKET
import MEMBER

while True:
    TRAIN.clrscreen()
    print("\t\t\t Railway management\n")
    print("====================================================================")
    print("1. Train management")
    print("2. Member management")
    print("3. Issue Ticket")
    print("4.Exit")
    print("====================================================================")
    choice=int(input("Enter choice between 1 to 4:"))
    if choice==1:
        RAILWAYMENU.menutrain()
    elif choice==2:
        RAILWAYMENU.menumember()
    elif choice==3:
        RAILWAYMENU.menuticket()
    elif choice==4:
        break
    else:
        print("Wrong choice, enter your choice again:")
        x=input("Enter any key to continue")
