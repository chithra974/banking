import mysql.connector

mydb=None
def connect():
    global mydb

mydb=mysql.connector.connect(
    host="localhost",
    user="root",
    password="chithra",
    database="bank")


def openacc():
    n=input("Enter Name  :")
    ac=input("Enter Account No  :")
    db=input("Enter Date Of Birth  :")
    ph=input("Enter phone Number :")
    ad=input("Enter Address   :")
    ob=int(input("Enter Opening Balance  :"))
    data1=(n,ac,db,ph,ad,ob)
    data2=(n,ac,ob) 
    sql1="insert into account values(%s,%s,%s,%s,%s,%s)"
    sql2="insert into amount values(%s,%s,%s)"
    cur=mydb.cursor()
    cur.execute(sql1,data1)
    cur.execute(sql2,data2)
    mydb.commit()
    print("Data Entered Suceessfully")
    main()



def depoAmo():
    am=int(input("Enter Amount  :"))
    ac=input("Enter Account No  :")
    a="select balance from amount where acno=%s"
    data=(ac) 
    cur=mydb.cursor()
    cur.execute(a,data)
    myresult=cur.fetchone()
    tam=myresult[0]+am
    sql="update amount set balance=%s where acno=%s"
    d=(tam,ac)
    cur.execute(sql,d)
    mydb.commit()
    main()    



def witham():
    am=int(input("Enter Amount  :"))
    ac=input("Enter Account No  :")
    a="select balance from amount where acno=%s"
    data=(ac) 
    cur=mydb.cursor()
    cur.execute(a,data)
    myresult=cur.fetchone()
    tam=myresult[0]-am
    sql="update amount set balance=%s where acno=%s"
    d=(tam,ac)
    cur.execute(sql,d)
    mydb.commit()
    main()    



def balance():
    ac=input("Enter Account No  :")
    a="select balance from amount where acno=%s"
    data=(ac,) 
    cur=mydb.cursor()
    cur.execute(a,data)
    myresult=cur.fetchone()
    print("Balance for Account :",ac," is ",myresult[0])
    main()    


def dispacc():
    ac=input("Enter Account No  :")
    a="select * from amount where acno=%s"
    data=(ac) 
    cur=mydb.cursor()
    cur.execute(a,data)
    myresult=cur.fetchone()
    for i in myresult:
        print(i,end=" ")
    main() 


def closeac():
    ac=input("Enter Account No  :")
    sql1="delete from amount where acno=%s"
    sql2="delete from amount where acno=%s"
    data=(ac) 
    cur=mydb.cursor()
    cur.execute(sql1,data)
    cur.execute(sql2,data)
    mydb.commit()
    main()    
   
def main():
    print(""" 
    1.OPEN NEW ACCOUNT 
    2.DEPOSIT AMOUNT
    3.WITHDRAW AMOUNT 
    4.BALANCE ENQUIRY 
    5.DISPLAY CUSTOMER DETAILS 
    6.CLOSE AN ACCOUNT
    """)
    choice=input("ENTER THE TASK NO:")
    if (choice=='1'):
       openacc()
    elif(choice=='2'):
        depoAmo()
    elif(choice=='3'):
        witham()
    elif(choice=='4'):
        balance()
    elif(choice=='5'):
        dispacc()
    elif(choice=='6'):
        closeac()
    else:
        print("wrong choice...") 
        main()
    main()                       


    
        






