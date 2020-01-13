#-*- coding: utf-8 -*-
#필요 List
UserID=[]
UserPW=[]
notborrowedList=[]
totalbookList=[]
borrowedList=[]
#함수들

#1. 디스플레이 보드
def display():
    print('''             ------------------------------
                         log-in
             ------------------------------
             ----------Book manage---------
             1). Book insert
             2). Book search
             3). Book delete
             4). Book sort
             5). Book total output
             6). User insert
             7). User delete
             8). Borrow
             9). return
             10). See borrowed book or not borrowed book

                                     '''   )
    return "Please select."

#2. 회원가입

def register(a,b):#함수 사용할때 a,b를 각각 아이디 패스워드로 놓고, 입력.
    if a in UserID and b in PW:
        print('Your address already exist.')
        print("---------------------")
        
    else:
        UserID.append(a)
        UserPW.append(b)
        print('Registeration is complete.')
        print("---------------------")
        
        

#3 로그인

def login(ID,PW):
    
    if ID in UserID and PW in UserPW:
        display()
    else:
        print('ID is not exist. Please register.')
        a=raw_input('ID:')
        b=raw_input('PW:')
        if a in UserID and b in UserPW:
            print('Your address already exist.')
        
        else:
            UserID.append(a)
            UserPW.append(b)
            print('Please log-in again.')
        a=raw_input('ID:')
        b=raw_input('PW:')
        login(a,b)






#소스코드
#1. 로그인과 보드

Stop=True
while Stop:
    print("log-in please.")
    ID=raw_input('ID:')
    PW=raw_input('PW:')
    login(ID,PW)
    print('Please input the number.(in 1~10)')
    print('if you want to quit this program, insert the number 0')
    print('')
    number=raw_input('input:')

    if number=='1':#Book insert.
        print('Insert the book name')
        Bookname=raw_input()
        if Bookname in totalbookList:
            print('the book is already exist')
            print('---------------------')
               
        else:
            notborrowedList.append(Bookname)
            totalbookList.append(Bookname)
            print('the book is added.')
            print("---------------------")

    elif number=='2':#Book search
        print('Insert the book name')
        Bookname=raw_input()
        if Bookname in notborrowedList or Bookname in totalbookList or Bookname in borrowedList:
            print('The book you are searching is in library.')
            print("---------------------")
        else:
            print('The book you are searching is not in library')
            print("---------------------")

    elif number=='3':#Book delete
        print('Insert the book name')
        Bookname=raw_input()
        if Bookname in notborrowedList:
            notborrowedList.remove(Bookname)
            totalbookList.remove(Bookname)
            print("The book is deleted")
            print("---------------------")
        elif Bookname in borrowedList:
            borrowedList.remove(Bookname)
            totalbookList.remove(Bookname)
            print("The book is deleted")
            print("---------------------")
        elif Bookname in totalbookList:
            totalbookList.remove(Bookname)
            print("The book is deleted")
            print("---------------------")

        else:
            print('The book you are searching is not in library')
            print("---------------------")

    elif number=='4':#Book sort
        print('Do you want to sort books?(y/n)')
        respond=raw_input()
        if respond=='y':
            totalbookList.sort()
            notborrowedList.sort()
            print('sortation complete.')
            print("---------------------")
        elif respond=='n':
            print('OK.')
            print("---------------------")
        else:
            print('Please insert correct value.')
            print("---------------------")

    elif number=='5':#Book total output
        print(totalbookList)
        print("---------------------")

    elif number=='6':#User insert (회원가입)
        print('please insert ID and PW.')
        q=raw_input('ID:')
        w=raw_input('PW:')
        register(q,w)

    elif number=='7':#User delete(회원 탈퇴) 
        print('please insert ID and PW.')
        ID1=raw_input('ID:')
        PW1=raw_input("PW:")
        if ID1 in UserID and PW1 in UserPW:
            UserID.remove(ID1)
            UserPW.remove(PW1)
            End2=True
            print('you must return the book you borrow.')
            print('Please insert the book you want to return')
            returnbook=raw_input(':')
            while End2:
                if returnbook in borrowedList:
                    print('Do you want to return? answer me y or n')
                    respond1=raw_input(':')
                    if respond1=='y':
                        borrowedList.remove(returnbook)
                        notborrowedList.append(returnbook)
                        print('Ok. you returned this book')
                        print("---------------------")
                        End2=False
                    elif respond1=='n':
                        print('Ok. Thank you!')
                        print("---------------------")
                        End2=False
                    else:
                        print('Please insert y or n')
                        print("---------------------")
                else:
                    print("Sorry, the book you want to return is not ours. or This book isn't borrowed.")
                    print("---------------------")
                    End2=False
            
            print('The process is done. your account is deleted. Thank you')
            print("---------------------")
        else:
            print('The account not exist in here.')
            print("---------------------")
    elif number=='8':#Borrow
        End=True
        
        print('Please insert the book you want to borrow')
        borrowbook=raw_input(':')
        while End:
            if borrowbook in notborrowedList:
                print('the book you are searching is not borrowed.')
                print('Do you want to borrow? answer me y or n')
                respond=raw_input(':')
                if respond=='y':
                        borrowedList.append(borrowbook)
                        notborrowedList.remove(borrowbook)
                        print('OK. you borrowed this book.')
                        print("---------------------")
                        End=False
                elif respond=='n':
                        print('ok. Thank you!')
                        print("---------------------")
                        End=False
                else:
                        print('Please insert y or n')
                        print("---------------------")
            
            
            else:
                print("sorry, the book you want to borrow is already borrowed. or We dosen't have this book")
                print("---------------------")
                End=False
                
    elif number=='9':#return
        End2=True
        print('Please insert the book you want to return')
        returnbook=raw_input(':')
        while End2:
            if returnbook in borrowedList:
                print('Do you want to return? answer me y or n')
                respond1=raw_input(':')
                if respond1=='y':
                    borrowedList.remove(returnbook)
                    notborrowedList.append(returnbook)
                    print('Ok. you returned this book')
                    print("---------------------")
                    End2=False
                elif respond1=='n':
                    print('Ok. Thank you!')
                    print("---------------------")
                    End2=False
                else:
                    print('Please insert y or n')
                    print("---------------------")
            else:
                print("Sorry, the book you want to return is not ours. or This book isn't borrowed.")
                print("---------------------")
                End2=False
            
    elif number=='10':# 빌린책과 빌리지 않은 책 보여주기
        print('If you want to view not borrowed books, please enter 1')
        print('or want to view borrowed books, please enter 2')
        Inputnum=raw_input('insert:')
        if Inputnum=='1':
            print(notborrowedList)
        elif Inputnum=='2':
            print(borrowedList)
        else:
            print('please input right number.')
    

    elif number=='0':#종료
            Stop=False

    else:#숫자말고 다른값 넣으면 다시넣으라고 해주는것.
        print('Please insert correct value.')
        print("---------------------")

