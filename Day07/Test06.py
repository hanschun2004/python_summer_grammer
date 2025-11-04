# 중국집 주문 프로그램
# 사용자에게 짜장면, 짬뽕 주문 수량을 입력받아 결제 금액을 계산하여 출력

# 짜장면 - 5000원
# 짬뽕 - 6000원

# 5그릇 이상 주문하면 3천원 할인되도록 금액을 계산하여 출력해주세요.
# 10그릇 이상 주문 하면 10% 할인 처리

a = int(input("짜장면 수량 입력 : "))
b = int(input("짬뽕 수량 입력 : "))
pay = a*5000+b*6000
print("원래 가격은 {} 입니다.".format(pay))
print("할인 적용을 하겠습니다.")

if a+b >=10:
    price = (a*5000+b*6000)*0.9
    print("10%할인 처리")
    print("{}원".format(price))
elif a+b>=5:
    price = (a*5000+b*6000)-3000
    print("3000할인 처리")
    print("{}원".format(price))
else:
    price = a*5000+b*6000
    print("{}원".format(price))

red = int(input("짜장면 수량 입력 : "))
black = int(input("짬뽕 수량 입력 : "))

tot = red + black # 주문수량 합계
rp = 6000
bp = 5000

cnt1 = 5
cnt2 = 10

rate1 = 3000 # 이렇게 변수를 따로 설정해야 나중에 값 바꿀때 쉬움 
rate2 = 10
price = rp * red + bp * black


if tot >= cnt2:
    print("{}그릇 이상 주문시 {} % 할인 !".format(cnt2,rate2))
    print("총 금액 : {}".format(int(price/100*(100-rate2))))
elif tot >= cnt1:
    print("{}그릇 이상 주문시 {}원 할인 !".format(cnt1,rate1))
    print("총 금액 : {}".format(price - rate2))
    






