#PYTHON MODULE: TICKET
import mysql.connector
from mysql.connector import errorcode
from datetime import date,datetime,timedelta
from mysql.connector import(connection)
import os
import platform

def clrscreen():
    print('\n'*5)
    
def showtickets():
    try:
        os.system('cls')
        cnx=connection.MySQLConnection(user="root",password="Tanisha2015",host="localhost",database="RAILWAY_RESERVATION_PROJECT_CS")
        Cursor=cnx.cursor()
        query=("SELECT *FROM TICKET")
        Cursor.execute(query)
        for x in Cursor:
            print("====================================================================")
            print("PNRCode:",x[0])
            print("Train code:",x[1])
            print("No. of persons:",x[2])
            print("No. of infants:",x[3])
            print("No.of children:",x[4])
            print("No. of adults:",x[5])
            print("No. of senior citizens:",x[6])
            print("Class:",x[7])
            print("Starting point:",x[8])
            print("End point:",x[9])
            print("No. of stations:",x[10])
            print("Total Fare:",x[11])
            print("Date of Departure:",x[12])
            print("Status:",x[13])
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

def issueticket():
    try:
        cnx=connection.MySQLConnection(user="root",password="Tanisha2015",host="localhost",database="RAILWAY_RESERVATION_PROJECT_CS")
        Cursor=cnx.cursor()
        PNRCODE=int(input("Enter PNR code of new ticket to  issue:"))
        TCODE=int(input("Enter Train code you choose:"))
        NOOFPERSONS=int(input("Enter No. of persons:"))
        INFANTS=int(input("Enter No. of infants:"))
        CHILDREN=int(input("Enter No. of children:"))
        ADULTS=int(input("Enter No. of adults:"))
        SENIORCITIZENS=int(input("Enter No. of Senior Citizens:"))
        CLASS=input("Choose class from AC1, AC2, AC3 and Sleeper class:")
        STARTPT=input("Enter the starting point:")
        ENDPT=input("Enter the end point:")
        NOOFKM=float(input("Enter the no. of kilometres you will travel:"))
        TOTALFARE=float(input("Enter total fare:"))
        print("Enter Date of Departure (Date/Month and Year seperately):")
        DD=int(input("Enter Date:"))
        MM=int(input("Enter Month:"))
        YY=int(input("Enter Year:"))
        DATE_OF_DEPART=date(YY,MM,DD)
        STATUS=input("Enter status:")
        Qry=("INSERT INTO TICKET VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)")
        data=(PNRCODE,TCODE,NOOFPERSONS,INFANTS,CHILDREN,ADULTS,SENIORCITIZENS,CLASS,STARTPT,ENDPT,NOOFKM,TOTALFARE,DATE_OF_DEPART,STATUS)
        Cursor.execute(Qry,data)
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

def deleteticket():
    try:
        cnx=connection.MySQLConnection(user="root",password="Tanisha2015",host="localhost",database="RAILWAY_RESERVATION_PROJECT_CS")
        Cursor=cnx.cursor()
        PNRCODE=int(input("Enter PNR Code of the ticket to be Cancelled:"))
        TCODE=int(input("Enter Train code:"))
        Qry=(" UPDATE TICKET SET STATUS='CANCELLED' WHERE PNRCODE=%s AND TCODE=%s""")
        rec=(PNRCODE,TCODE)
        Cursor.execute(Qry,rec)
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

