#-*- encoding: utf-8 -*-


def login():
    global START            #전역변수
    print('<login>')
    ID = raw_input('ID : ')
    if ID not in userinfo.keys():        #ID가 틀릴경우 사용자를 추가할지를 물음
        print ('The ID is not existed. Do you want to register? (no/yes)')
        register=raw_input()
        if register =='yes' or register=='y':
            userinsert()    #사용자를 추가한다고 하면 사용자추가함수 부름
            START=True
        else:
            START=False     #로그인 안하면 종료
            print('Bye')
    else:
        while 1:                #ID가 맞을 경우 비밀번호가 맞을때까지 입력
            password = raw_input('Password : ')  
            if password == userinfo.get(ID):
                print('Login success')
                START=True
                break
            else:
                print('Password is not correct.')
            


def bookinsert():
    name=raw_input('Book name : ')      #삽입할 책 제목 입력
    field=raw_input('field : ')         #삽입할 책 분야 입력
    bookinfo[name]= field               #책이름과 분야를 dictionary에 넣음
    bookname.append(name)               #책이름 리스트에 추가
    print('book is inserted successfully')

def booksearch():
    searchbook=raw_input('Book name : ')           #찾을 책 입력
    if searchbook in bookname:
        print('The book is existed')
    else:
        print('The book is not existed')
        
def bookdelete():
    deletebook=raw_input('Book name : ')        #삭제할 책 입력
    if deletebook in bookname:
        del bookinfo[deletebook]
        bookname.remove(deletebook)
        print('The book is deleted successfully')
    else:
        print('The book is not existed')

def booksort():
    bookname.sort()         #알파벳순으로 책이름 정렬
    print(bookname)
    
def output():
    print(bookinfo)         #책 정보 출력

def userinsert():
    while 1:
        ID = raw_input('user ID : ')
        if ID in userinfo.keys():
            print('This ID is already existed. Put another ID.')
                #ID가 중복되는지 검사
        else:
            break
    password=raw_input('user Password : ')
    userinfo[ID] = password                 #사용자정보 dictionary에 추가
    print('User is created successfully.')
    
def userdelete():
    print('Do you want to delete user really? (yes/no)')
    delete = raw_input()
    if delete=='yes' or delete=='y':
        ID=raw_input('your ID : ')
        if ID in userinfo.keys():
            del userinfo[ID]                #사용자 삭제
            print('%s is deleted.'%ID)
            login()
        else:
            print('The user is not existed')
    else:
        print('okay')
    
    
def borrowbook():
    name=raw_input('book name : ')
    if name in bookname:
        bookname.remove(name)
        borrowlist.append(name)      #책을 빌리면 빌려간책 목록으로 들어감
        print('The book is borrowed successfully')
    else:
        print('The book is not existed')
        
        
def returnbook():
    name=raw_input('book name : ')
    if name in borrowlist:
        borrowlist.remove(name)      #책을 반납하면 빌려간책 목록에서 없어짐.
        bookname.append(name)
        print('The book is returned successfully')
    else:
        print('The book is not existed')
    
def mybook():       
    print(borrowlist)                #내가 빌려간 책 목록 출력


bookinfo={}
bookname=[]
userinfo={'administrator' : '123'}  #사용자 ID를키값, 비밀번호를 value값으로함
borrowlist=[]


START=''
login()

while START:

    print """
    <Book manage>
    1. Book insert
    2. Book search
    3. Book delete
    4. Book sort
    5. Book total output
    6. User insert
    7. User delete
    8. Borrow book
    9. Return book
    10. My book list
    11. logout

    Choose the number you want to excute
    """
    
    number = int(raw_input('number : '))
    if number==1:
        print('<book insert>')
        bookinsert()
        
    elif number==2:
        print('<book search>')
        booksearch()
        
    elif number==3:
        print('<book delete>')
        bookdelete()
        
    elif number==4:
        print('<book sort>')
        booksort()
        
    elif number==5:
        print('<book total output>')
        output()
    elif number==6:
        print('<user insert>')
        userinsert()
        
    elif number==7:
        print('<user delete>')
        userdelete()
        
    elif number==8:
        print('<borrow book>')
        borrowbook()
        
    elif number==9:
        print('<return book>')
        returnbook()
        
    elif number==10:
        print('<my book list>')
        mybook()
        
    elif number==11:
        break
    
    else:
        print ("Choose the number from 1 to 11")
    


