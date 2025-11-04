# 1. input() 으로 2개의 값을 입력 받고
# 더하기, 빼기, 곱하기, 나누기(몫), 나누기(실수), 나누기(나머지)
# 연산을 하여 그 결과를 출력하는 코드를 작성하세요.

a = int(input("숫자1를 입력하세요 :"))
c = input("원하는 연산자를 입력하세요 :")
b = int(input("숫자2를 입력하세요 :"))
if c=="+":
    print("{} + {} = {}".format(a, b, a+b))
elif c=="-":
    print("{} - {} = {}".format(a, b, a-b))
elif c=="*":
    print("{} * {} = {}".format(a, b, a*b))
elif c=="//":
    print("{} // {} = {}".format(a, b, a//b))
elif c=="/":
    print("{} / {} = {:f}".format(a, b, a/b))
elif c=="%":
    print("{} % {} = {}".format(a, b, a%b))
    

    
