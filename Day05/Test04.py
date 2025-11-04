# 사용자로 부터 이름, 키, 체중 값을 입력 받아 비만도를 구하고
# 출력하는 코드를 작성하시오

# 비만도 계산식 : 비만도(%) = 현재 체중 / 표준 체중 * 100
# 표준 체중 계산식 : 표준 체중 = (현재 키 -100)*0.9

# 출력 예제 : 홍길동님의 비만도는 112.15% 입니다.

name = input("이름을 입력하세요 : ")
height = float(input("키를 입력하세요 : "))
weight = float(input("체중을 입력하세요 : "))

standard_weight = (height - 100)*0.9
bmi = (weight/standard_weight)*100

print("홍길동님의 비만도는 {:.2f}%입니다.".format(bmi))

from random import randrange
print("아무 수나 출력 {:d}".format(random.randrange(0,100)))
