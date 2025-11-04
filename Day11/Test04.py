menu = (("칼국수",6000),
        ("비빔밥",5500),
        ("돼지국밥",7000),
        ("돈까스",7000),
        ("김밥",2000),
        ("라면",2500))

# 위의 튜플 구조를 보고 아래에서 요구하는 값을 출력하는 코드를 작성하세요
# 김밥과 라면의 가격을 각각 출력하세요
# 인덱스 접해서 출력
print("{} : {}원".format(menu[4][0], menu[4][1]))
print("{} : {}원".format(menu[5][0], menu[5][1]))

# 가격이 7000원에 해당하는 메뉴를 출력하세요
# 반복문..
for i in menu:
    if i[1] == 7000:
            print("{} : {}원".format(i[0],i[1]))

for i in range(0,len(menu)):
    if menu[i][1] == 7000:
            print("{} : {}원".format(menu[i][0],menu[i][1]))
    
# 가격이 6000원 이하인 메뉴를 출력하세요
for i in menu:
    if i[1] <=6000:
        print("{} : {}원".format(i[0],i[1]))
              
for i in range(0,len(menu)):
    if menu[i][1] <= 6000:
            print("{} : {}원".format(menu[i][0],menu[i][1]))

            

# 사용자 입력으로 메뉴를 입력받아 해당하는 메뉴의 가격을 출력하세요.
'''
food = input("메뉴 입력 : ")
for i in range(0,6):
    if menu[i][0] == food:
        print(menu[i][1])
'''
user = input("메뉴 입력 : ")
for i in menu:
    if i[0] == user:
        print("{} : {}원".format(i[0],i[1]))

user = input("메뉴 입력 : ")
for i in range(len(menu)):
    if menu[i][0] == user:
        print("{} : {}원".format(menu[i][0],menu[i][1]))



# 사용자 입력으로 1개이상의 메뉴를 입력받아 해당 메뉴의 총 가격을 출력
# (exit를 입력하면 더이상의 입력은 받지 않는다.)
'''
price = 0
while food != "exit":
    food = input("메뉴 입력 : ")
    for i in range(0,6):
        if menu[i][0] == food:
            price += menu[i][1] 
print(price)
'''

tot = 0
while True:
    user = input("메뉴입력 : ")
    if user == "exit":
        break
    for i in menu:
        if i[0] == user:
            tot += i[1]
print("총 가격 : {}원".format(tot))



















































