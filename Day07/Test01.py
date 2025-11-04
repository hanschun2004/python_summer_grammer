# 수를 입력 받아 짝수이면서 3의 배수이면 출력

# 1. 짝수이면서 3의 배수입니다.
# 2. 짝수이면서 3의 배수가 아닙니다.
# 3. 홀수이면서 3의 배수입니다.
# 4. 홀수이면서 3의 배수가 아닙니다.

# and

# if 문에 if

'''
a = int(input("수 입력 : "))
if a % 2 == 0 and a % 3 ==0:
    print("짝수이면서 3의 배수입니다.")
if a % 2 == 0 and a % 3 !=0:
        print("짝수이면서 3의 배수가 아닙니다.")
if a % 2 !=0 and a % 3 ==0:
        print("홀수이면서 3의 배수입니다.")
if a % 2 !=0 and a % 3 !=0:
        print("홀수이면서 3의 배수가 아닙니다.")


a = int(input("수 입력 : "))
if a % 2 == 0:
    if a % 3 ==0:
        print("짝수이면서 3의 배수입니다.")
    else:
        print("짝수이면서 3의 배수가 아닙니다.")
        
else:
    if a % 3 ==0:
        print("홀수이면서 3의 배수입니다.")
    else:
        print("홀수이면서 3의 배수가 아닙니다.")

'''

su = int(input("숫자 입력 : "))

# and
if su%2==0 and su%3==0:
    print("{} - 짝수이면서 3의 배수입니다.".format(su))
if su%2==0 and su%3!=0:
    print("{} - 짝수이면서 3의 배수가 아닙니다.".format(su))
if su%2!=0 and su%3==0:
    print("{} - 홀수이면서 3의 배수입니다.".format(su))
if su%2!=0 and su%3!=0:
    print("{} - 홀수이면서 3의 배수가 아닙니다.".format(su))


# if 문 안에 if문
if su % 2==0: # 짝수
    if su %3==0:
        print("{} - 짝수이면서 3의 배수입니다.".format(su))
    else:
        print("{} - 짝수이면서 3의 배수가 아닙니다.".format(su))
else: # 홀수
    if su %3 ==0:
        print("{} - 홀수이면서 3의 배수입니다.".format(su))
    else:
        print("{} - 홀수이면서 3의 배수가 아닙니다.".format(su))

# 오 재밌는데 진짜 꿀잼이양






