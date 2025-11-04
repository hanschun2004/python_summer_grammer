# 1 ~ 100 까지의 누적합을 구하는 코드를 작성
tot = 0
for i in range(1,101):
    tot += i
    if i == 100:
        print(tot)

tot = 0
for i in range(1,101):
    tot += i
print(tot)


# 다음 문자열 변수에서 공백을 제외한 문자의 수를 구하시오
st = "Python basic program language"
'''
List =(st.split(" "))
tot = 0
for i in range(0,4):
    tot += len(List[i])
    if i == 3:
        print(tot)
'''

cnt = 0
for i in st:
    if i != ' ':
        cnt += 1
print(cnt)

cnt = 0
for i in range(len(st)):
    if st[i] == ' ':
        cnt += 1
print(len(st)-cnt)

        










