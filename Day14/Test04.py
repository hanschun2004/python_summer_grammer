# [문제 4]
'''
position = ['과장', '부장', '대리' , '사장', '대리' , '과장']
grade = [] 

for i in position:
    if grade.count(i) == 0:
        grade.append(i)
print("중복되지 않은 직위 : {}".format(grade))
dic = {}

for i in grade:  
    a = position.count(i)
    dic.update({i : a})
print("각 직위별 빈도수 : {}".format(dic))
'''
position = ['과장', '부장', '대리' , '사장', '대리' , '과장']
check = []
for i in position:
    if i not in check:
        check.append(i)
check.clear()
for i in range(len(position)):
    if check.count(position[i]) == 0:
        check.append(position[i])
print(check)

dic = {}
for i in range(len(position)):
    dic.update({position[i] : position.count(position[i])})
print(dic)

for i in position:
    st = i # st = "과장" , "부장" , "대리" , "사장" ..
    cnt = position.count(st) # position 리스트 안에 st 라는 문자열의 개수
    dic.update({st : cnt})
print(dic)

        







































