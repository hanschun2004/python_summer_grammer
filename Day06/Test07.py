# 두 수를 입력 받아서 큰수를 출력
# 단, 두개의 수가 동일하면 같다라고 출력하세요

a , b = int(input("수를 입력하세요 : ")), int(input("수를 입력하세요 : "))

if a > b:
    print("{} : {} -> {} ".format(a,b,a))
elif a < b:
    print("{} : {} -> {} ".format(a,b,b))
else:
    print("두 수가 동일하다")

if a > b:
    print("{} : {} -> {} ".format(a,b,a))
if a < b:
    print("{} : {} -> {} ".format(a,b,b))
if a == b:
    print("두 수가 동일하다")
`







