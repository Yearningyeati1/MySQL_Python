##MYSQL TABLE CREATION

'''
create database billing;

use billing;

create table Books(
BOOKID int primary key,
NAME varchar(20) not null,
R_WEEK float not null,
GENRE varchar(20) not null);

create table Transaction(
TRAN_ID int primary key,
BOOKID int not null,
SALEAMT float not null,
T_DATETIME datetime not null,
constraint cfk1 FOREIGN KEY(BOOKID) references Books (BOOKID) ON DELETE CASCADE);

create table Net(
BOOKID int unique,
TOTAL_SALES float default 0,
constraint cfk2 FOREIGN KEY(BOOKID) references Books(BOOKID) ON DELETE CASCADE);
'''

##PYTHON CODE BEGINS



def add_book():

    bid=int(input('Enter a BOOKID for book(must be unique and an integer:'))
    bn=input('Enter the name of the book:')
    rate=float(input('Enter the borrowing rate of the book per week:'))
    gn=input('Enter the book genre:')
    s='insert into books values({},"{}",{},"{}")'.format(bid,bn,rate,gn)
    cur=con.cursor()
    cur.execute(s)
    s2='insert into net values({},0)'.format(bid,)
    cur.execute(s2)
    print('Book inserted successfully\n')
    con.commit()
    
def del_book():

    id1=input('Enter BOOKID to delete the book:')
    s='delete from BOOKS where BOOKID={}'.format(id1,)
    cur=con.cursor()
    cur.execute(s)
    print('Record of book and associated records deleted successfully.')
    con.commit()
    

def create_transaction():
    
    import random
    print()
    id1=int(input('Enter BOOKID of Book:'))  
    cur=con.cursor()
    t='select name,r_week from books where bookid={};'.format(id1,)
    cur.execute(t)
    x=cur.fetchone()
    print(tabulate.tabulate([x],headers=['Book Name','Rate per Week'],tablefmt='psql'))
    rate=x[1]
    weeks=int(input('\nEnter number of weeks it will be rented for:'))
    price=weeks*rate
    print('\nSales amount=',price)
    t_id=random.randint(10000,50000)
    s='insert into transaction values({},{},{},now());'.format(t_id,id1,price)
    cur.execute(s)
    w='update net set total_sales=total_sales+{} where bookid={};'.format(price,id1)
    cur.execute(w)
    print('\nTransaction completed successfully!\n')
    print('For reference please note Transaction ID:',t_id,end='\n\n')
    con.commit()

def display_data():
    
    s='select * from books ;'
    cur=con.cursor()
    cur.execute(s)
    dat=cur.fetchall()
    h=['BOOKID','BOOKNAME','RENT/WEEK','GENRE']
    print('\nCurrent books in Database:')
    print(tabulate.tabulate(dat,headers=h,tablefmt='psql'))

def update_book():
    
    bid=int(input('Enter BOOKID of Book to update its Data:'))
    s='select * from books where bookid={};'.format(bid,)    
    cur=con.cursor()
    cur.execute(s)
    dat=cur.fetchone()
    print('\nCurrent data in database:\n')
    x=['BOOKID','BOOKNAME','RENT PER WEEK','GENRE']
    print(tabulate.tabulate([dat],x,tablefmt='psql'))
    ch=input('Do you wish to continue update operation?(Y/N):')
    if ch in('y','Y'):
        nr=float(input('Enter New Rent\Week of Book:'))
        ng=input('Enter New Genre of the Book:')
        k='update books set R_week={},Genre="{}" where bookid={};'.format(nr,ng,bid)
        cur.execute(k)
        con.commit()
        print('\nOperation executed sucessfully.\n')
        
    else:
        print('Operation Cancelled.')

def refer_trans():
    
    tid=int(input('Enter transaction number to extract its details:'))
    s='select tran_id,books.BOOKID,name,saleamt,T_datetime from transaction,books where tran_id={} and transaction.bookid=books.bookid;'.format(tid,)
    cur=con.cursor()
    cur.execute(s)
    dat=cur.fetchall()
    h=['TRAN_ID','BOOKID','BNAME','SALE_AMOUNT','DATE_TIME']
    print(tabulate.tabulate(dat,h,tablefmt='psql'),end='\n\n')

def show_struc():
    
    x=['books','transaction','net']
    for y in x:
        s='desc '+y+';'
        cur=con.cursor()
        cur.execute(s)
        dat=cur.fetchall()
        print('Table:',y.upper())
        print(tabulate.tabulate(dat,['Fields','Type','Null','Key','Default','Extra'],tablefmt='psql'))

def genre_pop():
    
    s='select genre,sum(total_sales) as s from net natural join books group by genre order by s desc;'
    cur=con.cursor()
    cur.execute(s)
    dat=cur.fetchall()
    print('Genre Popularity Indicated By Total Sales:')
    print(tabulate.tabulate(dat,['Genre','Total_Sales'],tablefmt='fancy_grid'))

        

def transaction_record():
    
    bid=int(input('Enter BOOKID of Book to Transaction History:'))
    s='select * from transaction where bookid={};'.format(bid,)    
    cur=con.cursor()
    cur.execute(s)
    dat=cur.fetchall()
    x=['TRAN_ID','BOOK_ID','SALE_AMT','T_DATETIME']
    print("\nTransaction history of BOOKID:", bid)
    print(tabulate.tabulate(dat,x,tablefmt='psql'),end='\n\n')


def sales_rankbook():
    
    s='select net.bookid,name,Total_sales from books,net where net.bookid=books.bookid order by Total_sales desc;'    
    cur=con.cursor()
    cur.execute(s)
    dat=cur.fetchall()
    x=['BOOK_ID','BOOK_NAME','TOTAL_SALES']
    print(tabulate.tabulate(dat,x,tablefmt='psql'))   

#_MAIN_
import mysql.connector as connec
import tabulate as tabulate

print('***WELCOME TO LIBRARY BILLING v1.1***')
pasw=input('Enter your MySQl Passwoord:')
con=connec.connect(host="localhost",
user="root", passwd =pasw,database='billing')
if con.is_connected():
    print('**Connection established Successfully!**\n')

functions=[(1,'ADD BOOK'),(2,'DELETE BOOK'),(3,'MODIFY BOOK'),(4,'SHOW BOOKS'),(5,'PERFORM A TRANSACTION'),
                         (6,'REFER A TRANSACTION'),(7,'SHOW TRANSACTION RECORDS OF A BOOK'),(8,'SHOW GENRE POPULARITY BASED ONSALES'),
                         (9,'RANK BOOKS BASED ON TOTAL SALES'),(10,'EXIT PROGRAM')]


while True:

    print('\t*** M A I N   M E N U***')
    print(tabulate.tabulate(functions,['CHOICE','FUNCTION'],tablefmt='grid'))
    ch=int(input('\nENTER YOUR CHOICE:'))
    print()

    
    if ch==1:
        ch1=input('ARE YOU SURE YOU WANT TO ADD A BOOK?(Y/N):')
        if ch1 in('Y','y'):
            add_book()
            print()

        else:
            continue
        
    elif ch==2:
        ch1=input('ARE YOU SURE YOU WANT TO DELETE A BOOK?(Y/N):')
        if ch1 in('Y','y'):
            del_book()
            print()

        else:
            continue
        
    elif ch==3:
        ch1=input('ARE YOU SURE YOU WANT TO MODIFY A BOOK?(Y/N):')
        if ch1 in('Y','y'):
            update_book()
            print()

        else:
            continue
        
    elif ch==4:
        
        display_data()
        print('\n')


    elif ch==5:
        ch1=input('ARE YOU SURE YOU WANT TO PERFORM A TRANSACTION?(Y/N):')
        if ch1 in('Y','y'):
            create_transaction()
            print()

        else:
            continue
        
    elif ch==6:
        refer_trans()

    elif ch==7:
        transaction_record()
        
    elif ch==8:
        genre_pop()
        print('\n')

    elif ch==9:
        sales_rankbook()
        print()

    elif ch==10:
        print('***Thank you for using LIBRARY BILLING v1.0*** \n***PROGRAM TERMINATED***')
        con.close()
        break

    else:
        print("Invalid Input.")

    


        
