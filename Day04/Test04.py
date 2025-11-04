# 논리 연산
# 서로다른 논리값을 이용하여 새로운 논리값을 만들어 낸다.
# A and B : A도 True, B도 True이면 전체 결과 True
# A or B : A가 True이거나 혹은, B가 True이면 전체결과 True

age = 23
gender = "남성"
goToArmy = (age>=20) and (gender =="남성")
print("현역 입영 대상입니까?",goToArmy)

# and : 논리곱
# True : 1 False : 0
# 0과 1의 곱이라고 생각하면 편함

cash = 500
card = 1
canGoHomeByTaxi = (cash >=5000) or (card == 1)
print("택시 타고 집에 가기 :",canGoHomeByTaxi)
# or : 논리 합

# 값의 범위를 나타내는 조건
# ex) 입력받은 점수가 0점에서 100점 사이이면 점수와 True을 출력
score = 100
flag = (0<=score and score<=100)
flag = (0<=score<=100) # 파이썬만 가능
print("점수가 범위안에 있나요?", flag,score)


