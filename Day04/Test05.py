# 삼항 논리 연산자
# (조건) and "참" or "거짓"
# 조건에 따라서 참의 값이 되거나, 거짓의 값이 된다.

num = 100
oddEven = (num % 2 == 0) and "짝수" or "홀수" # or 옆에는 거짓일때를 적는다.
print("{} : {}".format(num,oddEven))

# 나이에 따라서 성인.미성년자 여부를 문자열 변수에 저장하고
# 화면에 출력하세요
age = 19

# 입력 받은 글자가 연산자 인지 아닌지 여부 출력
# 1) 경우의 수가 몇가지인가 
# 2) 모든경우의 수를 동시에 만족하는가, 하나만 만족하는가
# + , - , * , % , /

age_judge = (age >=20) and "성인" or "미성년자"
age_judge = (age < 20) and "미성년자" or "성인"
print("내 나이는 {}살이고 {}입니다".format(age, age_judge))

operator = "%"
isoperator = (operator == "+" or
                  operator == "-" or
                  operator == "*" or
                  operator == "%" or
                  operator == "/") and "연산자" or "문자열"

print("입력하신 문자는 {} 이고 {}입니다".format(operator, isoperator))

# 변수안에 bool(논리)값이 있으면 비교 연산 X


ch = "%"
isoperator = (ch == "+") or (ch == "-") or (ch == "*") or (ch == "%") or (ch == "/")
msg = isoperator and "연산자입니다" or "연산자가 아닙니다"
print(msg)


ch = "%"
isoperator = (ch != "+") and (ch != "-") and (ch != "*") and (ch != "%") and (ch != "/")
msg = isoperator and "연산자가 아닙니다" or "연산자입니다"
print(msg)

















