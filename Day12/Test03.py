menu = [['칼국수' , 6000] ,
        ['비빔밥' , 5500] ,
        ['돼지 국밥' , 7000] ,
        ['돈까스' , 7000] ,
        ['김밥' , 2000] ,
        ['라면' , 2500]]

# 위의 리스트 구조를 보고 아래에서 요구하는 결과가 반영되도록 코드를 작성하세요.
# 비빔밥과 돈까스의 가격을 출력하세요
'''
print("{} : {}원".format(menu[1][0] ,menu[1][1]))
print("{} : {}원".format(menu[3][0] ,menu[3][1]))

# 사용자의 입력으로 메뉴와 가격을 입력 받아 menu 변수에 자료를 추가하는 코드를 작성하세요
user_menu = input("메뉴 입력 : ")
user_price = int(input("가격 입력 : "))
menu.append([user_menu, user_price])
print(menu)
'''


# 사용자 입력으로 메뉴와 가격을 입력 받아 menu 변수에 자료를 추가할때
# 기존에 동일한 메뉴가 존재하는 경우 가격만 변경되도록 코드를 작성하세요
'''
user = input("메뉴 입력 : ")
price = int(input("가격 입력 : "))
check = True # bool

for i in range(0, len(menu)):
    if  menu[i][0] == user:
        menu[i][1] = price
        check = False
if check:
    menu.append([user, price])
print(menu)

'''
'''
user = input("메뉴 입력 : ")
price = int(input("가격 입력 : "))
check = 0

for i in menu:
    if  i[0] == user:
        i[1] = price
        check = 1
if check == 0:
    menu.append([user,price])
print(menu)  

'''
'''
user = input("메뉴 입력 : ")
price = int(input("가격 입력 : "))
i = 0

for i in range(len(menu)):
    if  menu[i][0] == user:
        menu[i][1] = price
        break
if i == len(menu)-1:
    menu.append([user,price])
print(menu)

'''     

# 메뉴를 자동으로 선택하여 출력하는 코드를 작성하세요.

import random
idx = int(random.random() * len(menu))
print("{} : {}원".format(menu[idx][0], menu[idx][1]))







































