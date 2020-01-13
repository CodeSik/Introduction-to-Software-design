#-*- coding: utf-8 -*-
def welcome ():
    print('''''======패스트 푸드 무인 주문 시스템=======
            ============= M E N U ============== 
    1.불고기 버거 가격:3000  2.새우버거 가격:2500  3.치킨버거 가격:3400
    4.감자튀김 가격:1500  5.치즈스틱 가격:1400  6.더블 치킨 버거 가격:3800
    7.콜라 가격: 1000  8.사이다 가격:1000  9.소프트 아이스크림 가격:500''''')
menus=[('불고기버거', 3000),('새우버거',2500),('치킨버거', 3400),('감자튀김',1500),('치즈스틱',1400),('더블 치킨버거',3800),('콜라',1000),('사이다',1000),('소프트 아이스크림',500)]
order=[]
count=0
ordercount=0
while ordercount <=10:
    welcome()
    num=int(input('주문하실 수량을 입력해 주세요 :'))
    while count < num :
        menu=int(input('메뉴를 선택하여 주세요 :'))
        order.append(menus[menu-1])
        count+=1
    sum=0

    print('구매내역 :', order)
    for p in range(0,len(order)):
        sum+=order[p][1]

    print('총 금액 :',sum)

    money=int(input('금액을 넣어주세요.:'))

    while money < sum :
        money+=int(input('금액이 부족합니다. 추가로 금액을 투입하여주십시오.:'))
    print('거스름돈은',money-sum,'원 입니다.',sep='')

    ask=input('주문을 종료하시겠습니까? [Y/N]')

    if ask == 'Y' :
        print('맛있는 식사 되십시오.')
        break
    elif ask == 'N' :
        order=[]
        count=0
        sum=0
        menu=[]
        ordercount+=1
        welcome()
    else :
        print('Y나  N를 입력해주십시오. 기기가 종료됩니다.')
        break
if ordercount == 11:
    print('''===================================================
주문 가능 횟수가 모두 소진되었습니다. 다음에 또오세요^^!''')
