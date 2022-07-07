#PYTHON MODULE : TRAIN
from mysql.connector import errorcode
from datetime import date, datetime,timedelta
from mysql.connector import(connection)
import os
import platform
import mysql.connector

def clrscreen():
    if platform.system()=="Windows":
        print(os.system("cls"))

def display():
    try:
        os.system('cls')
        cnx=connection.MySQLConnection(user="root",password="Tanisha2015",host="localhost",database="RAILWAY_RESERVATION_PROJECT_CS")
        Cursor=cnx.cursor()
        query=("SELECT*FROM TRAIN")
        Cursor.execute(query)
        for x in Cursor:            
            t=list(x)
            print("====================================================================")
            print("Train code:",x[0])
            print("Train name:",x[1])
            print("Starting point:",x[2])
            print("Ending point:",x[3])
            print("AC 1 Seats:",x[4])
            print("AC 2 Seats:",x[5])
            print("AC 3 Seats:",x[6])
            print("Sleeper Seats:",x[7])
            print("Fare per kilometres:",x[8])
            print("No of stations:",x[9])
            print("====================================================================")
        Cursor.close()
        cnx.close()
        print("You have done it!")
    except mysql.connector.Error as err:
        if err.errno==errorcode.ER_ACCESS_DENIED_ERROR:
            print("Something is wrong with your username or password")
        elif err.errno==errorcode.ER_BAD_DB_ERROR:
            print("Database does not exist")
        else:
            print(err)
    else:
        cnx.close()


def insertdata():
    try:
        cnx=connection.MySQLConnection(user="root",password="Tanisha2015",host="localhost",database="RAILWAY_RESERVATION_PROJECT_CS")
        Cursor=cnx.cursor()
        TCODE=int(input("Enter Train code in integers:"))
        TNAME=input("Enter Train name:")
        STARTPT=input("Enter Starting point:")
        ENDPT=input("Enter Ending point:")
        AC1SEATS=int(input("Enter AC 1 Seats:"))
        AC2SEATS=int(input("Enter AC 2 Seats:"))
        AC3SEATS=int(input("Enter AC 3 Seats:"))
        SLPRSEATS=int(input("Enter Sleeper Seats:"))
        FAREPERKM=float(input("Enter Fare per kilometres:"))
        NOOFSTATIONS=int(input("Enter No. of stations:"))
        data=(TCODE,TNAME,STARTPT,ENDPT,AC1SEATS,AC2SEATS,AC3SEATS,SLPRSEATS,FAREPERKM,NOOFSTATIONS)
        Qry=("INSERT INTO TRAIN VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)")        
        Cursor.execute(Qry,data)
        cnx.commit()
    #Make sure data is committed to the database cnx.commit()
        Cursor.close()
        cnx.close()
        print("Record Inserted")
    except mysql.connector.Error as err:
        if err.errno==errorcode.ER_ACCESS_DENIED_ERROR:
            print("Something is wrong with your username or password")
        elif err.errno==errorcode.ER_BAD_DB_ERROR:
            print("Database does not exist")
        else:
            print(err)
    cnx.close()
    
def deletedata():
    try:
        cnx=connection.MySQLConnection(user="root",password="Tanisha2015",host="localhost",database="RAILWAY_RESERVATION_PROJECT_CS")
        Cursor=cnx.cursor()
        TCODE=int(input("Enter Train Code of Train to be deleted from the Table:"))
        del_rec=(TCODE,)
        Qry=("DELETE FROM TRAIN WHERE TCODE=%s")        
        Cursor.execute(Qry,del_rec)
    #Make sure data is committed to the database
        cnx.commit()
        Cursor.close()
        cnx.close()
        print(Cursor.rowcount,"Record(s) Deleted Successfully")
    except mysql.connector.Error as err:
        if err.errno==errorcode.ER_ACCESS_DENIED_ERROR:
            print("Something is wrong with your username or password")
        elif err.errno==errorcode.ER_BAD_DB_ERROR:
            print("Database does not exist")
        else:
            print(err)
    cnx.close()
    
def searchtrainrec():
    try:
        cnx=connection.MySQLConnection(user="root",password="Tanisha2015",host="localhost",database="RAILWAY_RESERVATION_PROJECT_CS")
        Cursor=cnx.cursor()
        TCODE=input("Enter Train Code to be Searched from the Table:")
        query=("SELECT*FROM TRAIN WHERE TCODE=%s")
        rec_srch=(TCODE,)
        Cursor.execute(query,rec_srch)
        Rec_count=0
        for (TCODE,TNAME,STARTPT,ENDPT,AC1SEATS,AC2SEATS,AC3SEATS,SLPRSEATS,FAREPERKM,NOOFSTATIONS) in Cursor:
            Rec_count+=1
            print("====================================================================")
            print("Train code:",TCODE)
            print("Train name:",TNAME)
            print("Starting point:",STARTPT)
            print("Ending point:",ENDPT)
            print("AC 1 Seats:",AC1SEATS)
            print("AC 2 Seats:",AC2SEATS)
            print("AC 3 Seats:",AC3SEATS)
            print("Sleeper Seats:",SLPRSEATS)
            print("Fare per kilometres:",FAREPERKM)
            print("No of stations:",NOOFSTATIONS)
            print("====================================================================")
            if Rec_count%2==0:
                input("Press any key to continue")
                clrscreen()
        print(Rec_count,"Record(s) found")
    #Make sure data is committed to the database cnx.commit()
        Cursor.close()
        cnx.close()
    except mysql.connector.Error as err:
        if err.errno==errorcode.ER_ACCESS_DENIED_ERROR:
            print("Something is wrong with your username or password")
        elif err.errno==errorcode.ER_BAD_DB_ERROR:
            print("Database does not exist")
        else:
            print(err)
    cnx.close()
    
def updaterec():
    try:
        cnx=connection.MySQLConnection(user="root",password="Tanisha2015",host="localhost",database="RAILWAY_RESERVATION_PROJECT_CS")
        Cursor=cnx.cursor()
        TCODE=input("Enter Train Code of Train to be Updated from the Table:")
        T=int(TCODE)
        rec_srch=(TCODE,)
        query=("SELECT*FROM TRAIN WHERE TCODE=%s")
        Cursor.execute(query,rec_srch)
        for x in Cursor:            
            t=list(x)
            print("====================================================================")
            print("Train code:",x[0])
            print("Train name:",x[1])
            print("Starting point:",x[2])
            print("Ending point:",x[3])
            print("AC 1 Seats:",x[4])
            print("AC 2 Seats:",x[5])
            print("AC 3 Seats:",x[6])
            print("Sleeper Seats:",x[7])
            print("Fare per kilometres:",x[8])
            print("No of stations:",x[9])
            print("====================================================================")
        print("Enter new data:")
        TNAME=input("Enter Train name:")
        STARTPT=input("Enter Starting point:")
        ENDPT=input("Enter Ending point:")
        AC1SEATS=int(input("Enter AC 1 Seats:"))
        AC2SEATS=int(input("Enter AC 2 Seats:"))
        AC3SEATS=int(input("Enter AC 3 Seats:"))
        SLPRSEATS=int(input("Enter Sleeper Seats:"))
        FAREPERKM=float(input("Enter Fare per kilometres:"))
        NOOFSTATIONS=int(input("Enter No. of stations:"))
        print(TNAME,STARTPT,ENDPT,AC1SEATS,AC2SEATS,AC3SEATS,SLPRSEATS,FAREPERKM,NOOFSTATIONS,T)           
        data=(TNAME,STARTPT,ENDPT,AC1SEATS,AC2SEATS,AC3SEATS,SLPRSEATS,FAREPERKM,NOOFSTATIONS,T)
        Qry=("UPDATE TRAIN SET TNAME=%s,STARTPT=%s,ENDPT=%s,AC1SEATS=%s,AC2SEATS=%s,AC3SEATS=%s,SLPRSEATS=%s,FAREPERKM=%s,NOOFSTATIONS=%s WHERE TCODE=%s")
        Cursor.execute(Qry,data)
    #Make sure data is committed to the database
        cnx.commit()
        Cursor.close()
        cnx.close()
        print(Cursor.rowcount,"Record(s) Updated successfully")
    except mysql.connector.Error as err:
        if err.errno==errorcode.ER_ACCESS_DENIED_ERROR:
            print("Something is wrong with your username or password")
        elif err.errno==errorcode.ER_BAD_DB_ERROR:
            print("Database does not exist")
        else:
            print(err)
        cnx.close()
       
