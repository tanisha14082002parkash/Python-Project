#PYTHON MODULE: RAILWAYMENU
import TRAIN
import MEMBER
import TICKET

def menutrain():
    while True:
        TRAIN.clrscreen()
        print("\t\t\t Train Record Management \n")
        print("====================================================================")
        print("1.Add Train Record")
        print("2.Display Train Records")
        print("3.Search Train Record")
        print("4.Delete Train Record")
        print("5.Update Train Record")
        print("6.Return to Main Menu")
        print("====================================================================")
        choice=int(input("Enter choice between 1 to 6:"))
        if choice==1:
            TRAIN.insertdata()
        elif choice==2:
            TRAIN.display()
        elif choice==3:
            TRAIN.searchtrainrec()
        elif choice==4:
            TRAIN.deletedata()
        elif choice==5:
           TRAIN.updaterec()
        elif choice==6:
            return
        else:
            print("Wrong choice, enter your choice again:")
            x=input("Enter any key to continue")
            
def menumember():
     while True:
        TRAIN.clrscreen()
        print("\t\t\t Member Record Management \n")
        print("====================================================================")
        print("1.Add Member Record")
        print("2.Display Member Records")
        print("3.Search Member Record")
        print("4.Delete Member Record")
        print("5.Go to Main Menu")
        print("====================================================================")
        choice=int(input("Enter choice between 1 to 5:"))
        if choice==1:
            MEMBER.insertmember()
        elif choice==2:
            MEMBER.display()
        elif choice==3:
            MEMBER.searchmember()
        elif choice==4:
            MEMBER.deletemember()
        elif choice==5:
            return
        else:
            print("Wrong choice, enter your choice again:")
            x=input("Enter any key to continue")

def menuticket():
    while True:
        TRAIN.clrscreen()
        print("\t\t\t Ticket Record Management \n")
        print("====================================================================")
        print("1.Book Ticket")
        print("2.Display Issued Ticket Records")
        print("3.Cancel Ticket")
        print("4.Return to Main Menu")
        print("====================================================================")
        choice=int(input("Enter choice between 1 to 4:"))
        if choice==1:
            TICKET.issueticket()
        elif choice==2:
            TICKET.showtickets()
        elif choice==3:
            TICKET.deleteticket()
        elif choice==4:
            return
        else:
            print("Wrong choice, enter your choice again:")
            x=input("Enter any key to continue")
