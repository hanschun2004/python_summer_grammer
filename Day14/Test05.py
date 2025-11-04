# 가수 이름, 구성원 수 입력 받고 출력 까지 할 수 있도록 코딩
# (5명만 입력하고 출력하세요)

dic ={}

while True:
    name = input("가수 입력 : ")
    su = int(input("구성원 수 : "))
    if dic.get(name) == None:
        dic.update({name:su})
        print("정보가 입력 되었습니다.")
    else:
        print("동일한 가수 이름이 있습니다.")
    if len(dic) == 5:
        break

for key in dic:
    print("{} : {}명".format(key, dic[key]))

    


































