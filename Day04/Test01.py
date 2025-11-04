# 산술 연산 : 숫자 값을 계산하기 위한 연산자 ( 문자열도 가능 )

n1 , n2 = 10 , 3
print("{} + {} = {}".format(n1 , n2 , n1+n2)) # 덧셈
print("{} - {} = {}".format(n1 , n2 , n1-n2))# 뺄셈
print("{} * {} = {}".format(n1 , n2 , n1*n2)) # 곱셈
print("{} / {} = {}".format(n1 , n2 , n1/n2))  # 나눗셈(실수)
print("{} // {} = {}".format(n1 , n2 , n1//n2)) # 나눗셈 (몫)
print("{} % {} = {}".format(n1 , n2 , n1%n2)) # 나눗셈 (나머지)
print("{} ** {} = {}".format(n1 , n2 , n1**n2)) # 제곱

# 문자열 산술 연산
text = "Python!!"
print(text + "Hello") # 문자열 이어붙이기
print(text * 3)

# print(text+3)
# 숫자 + 숫자 (O)
# 문자열 + 문자열 (O)
# 숫자 + 문자열 (X)
# TypeError: can only concatenate str (not "int") to str

# print(text*'A')
# print(text*1.2)
# TypeError: can't multiply sequence by non-int of type 'str'

n1 = "10"
n2 = "20"
print("{} + {} = {}".format(n1, n2, n1+n2))
print("{} + {} = {}".format(n1, n2, int(n1) + int(n2)))

# 나머지 연산
# 1) 홀짝 연산, 배수 ,약수
# 2) 정수의 자릿수 구분
# 3) 랜덤수의 점위 제한 ( C언어 )

n1 = 500
n2 = -511
print(n1 % 2) # 짝수는 2로 나눈 나머지의 값이 항상 0
print(n2 % 2) # 홀수는 2로 나눈 나머지의 값이 항상 1

# 배수
n1 = 27
print(n1%3) # 3의 배수이기 때문에 나머지가 0

# 정수 자릿수 구분
birth = 230711
# 년 월 일을 구분해서 출력해보세요
# ex) 23년 7월 11일

day = birth % 100 # 나머지 연산으로 원하는 만큼의 자릿수 추출 가능
birth = birth // 100 # 대입 응용
month = birth % 100
year = birth // 100

print("{:d}년 {}월 {}일".format(year, month, day))
































