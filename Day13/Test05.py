# 다음의 메뉴와 가격을 key와 value로 사용하여 사전형 자료를 만드세요.
# 변수명은 menu
# 칼국수 - 6000원 , 비빔밥 - 5000원 , 돼지 국밥 - 7000원,
# 돈까스 - 7000원 , 김밥 - 2000원 , 라면 - 2500원

menu ={'칼국수' : 6000,
       '비빔밥' : 5000,
       '돼지 국밥' : 7000,
       '돈까스' : 7000,
       '김밥' : 2000,
       '라면' : 2500
       }


# 위에서 만든 사전형 자료 menu변수에서 가격이 6000원 미만에 해당하는
# 메뉴와 가격을 출력하는 코드를 작성하세요
'''
for name in menu: # '칼국수' : 6000
    if menu[name] < 6000:
        print("{} : {}".format(name,(menu[name])))
'''
for key in menu:
    if menu[key] < 6000:
        print("{} : {}".format(key,menu[key]))

# 사용자 입력으로 메뉴와 가격을 입력 받아 menu 변수에 자료를 추가할 수 있도록
# 하세요. (동일한 메뉴는 가격만 변경)

user = input("메뉴 입력 : ")
price = int(input("가격 입력 : "))
menu.update({user : price})
print(menu)


# 메뉴를 자동으로 선택하여 출력하는 코드를 작성하세요.
'''
import random
key = menu.keys()
ls = list(key)
rand = random.randint(0,5)    
print("{} : {}원".format(ls[rand], menu[ls[rand]]))
'''

import random
key = list(menu.keys())
idx = int(random.random() * len(key))
print("{} : {}원".format(key[idx] , menu[key[idx]]))




























