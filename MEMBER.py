#PYTHON MODULE: MEMBER
from mysql.connector import errorcode
from datetime import date,datetime,timedelta
from mysql.connector import(connection)
import os
import platform
import mysql.connector

def clrscreen():
    print('\n'*5)
    
def display():
    try:
        os.system('cls')
        cnx=connection.MySQLConnection(user="root",password="Tanisha2015",host="localhost",database="RAILWAY_RESERVATION_PROJECT_CS")
        Cursor=cnx.cursor()
        query=("SELECT*FROM MEMBER")
        Cursor.execute(query)
        for x in Cursor:
            t=list(x)
            print("====================================================================")
            print("PNR Code:",x[0])
            print("Member Name:",x[1])
            print("Age:",x[2])
            print("Address:",x[3])
            print("No. of persons:",x[4])
            print("Train code:",x[5])
            print("Status:",x[6])
            print("Mobile No. of Member:",x[7])            
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

def insertmember():
    try:
        cnx=connection.MySQLConnection(user="root",password="Tanisha2015",host="localhost",database="RAILWAY_RESERVATION_PROJECT_CS")
        Cursor=cnx.cursor()
        PNRCODE=int(input("Enter your PNR Code:"))
        MNAME=input("Enter Member Name:")
        AGE=int(input("Enter age"))
        PHONENO=int(input("Enter your phone no.:"))
        ADDRESS=input("Enter address:")
        NOOFPERSONS=int(input("Enter no. of persons:"))
        TCODE=int(input("Enter Train code:"))
        STATUS=input("Enter Status")        
        Qry=("INSERT INTO MEMBER VALUES (%s,%s,%s,%s,%s,%s,%s,%s)")
        data=(PNRCODE,MNAME,AGE,ADDRESS,NOOFPERSONS,TCODE,STATUS,PHONENO)
        Cursor.execute(Qry,data)
    #Make sure data is committed to the database
        cnx.commit()
        Cursor.close()
        cnx.close()
        print("Record Inserted.")
    except mysql.connector.Error as err:
        if err.errno==errorcode.ER_ACCESS_DENIED_ERROR:
            print("Something is wrong with your username or password")
        elif err.errno==errorcode.ER_BAD_DB_ERROR:
            print("Database does not exist")
        else:
            print(err)
    cnx.close()
        
def deletemember():    
    try:
        cnx=connection.MySQLConnection(user="root",password="Tanisha2015",host="localhost",database="RAILWAY_RESERVATION_PROJECT_CS")
        Cursor=cnx.cursor()
        PNRCODE=input("Enter PNR Code to be cancelled from the Table:")
        del_rec=(PNRCODE,)
        Qry=("UPDATE MEMBER SET STATUS='CANCELLED' WHERE PNRCODE=%s")        
        Cursor.execute(Qry,del_rec)
    #Make sure data is committed to the database
        cnx.commit()
        Cursor.close()
        cnx.close()
        print(Cursor.rowcount,"Record(s) Deleted successfully")
    except mysql.connector.Error as err:
        if err.errno==errorcode.ER_ACCESS_DENIED_ERROR:             
            print("Something is wrong with your username or password")
        elif err.errno==errorcode.ER_BAD_DB_ERROR:
            print("Database does not exist")
        else:
            print(err)
    cnx.close()

def searchmember():
    try:
        cnx=connection.MySQLConnection(user="root",password="Tanisha2015",host="localhost",database="RAILWAY_RESERVATION_PROJECT_CS")
        Cursor=cnx.cursor()
        PNRCODE=input("Enter PNR Code to be searched from the Table:")
        query=("SELECT*FROM MEMBER WHERE PNRCODE=%s")
        rec_srch=(PNRCODE,)
        Cursor.execute(query,rec_srch)
        Rec_count=0
        for (PNRCODE,MNAME,AGE,ADDRESS,NOOFPERSONS,TCODE,STATUS,PHONENO) in Cursor:
            Rec_count+=1
            print("====================================================================")
            print("PNR Code:",PNRCODE)
            print("Member Name:",MNAME)
            print("Age:",AGE)
            print("Address:",ADDRESS)
            print("No. of persons:",NOOFPERSONS)
            print("Train code:",TCODE)
            print("Status:",STATUS)
            print("Mobile No. of Member:",PHONENO)
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
                
