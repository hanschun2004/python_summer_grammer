# 정수 입력 후 정수가 홀수인지 짝수인지 출력하는 if 문을 작성

num = int(input("숫자를 입력하시오. : "))

if (num % 2 ==0):
          print("숫자 {}은 짝수 입니다.".format(num))
else:
    print("숫자 {}은 홀수 입니다.".format(num))


su = int(input("숫자를 입력하시오. : "))          
if su % 2 ==0:
          print("짝수")
if su %2 ==1:
    print("홀수")
          
