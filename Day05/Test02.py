# IO - Input / Output - 입출력

# 입력

# input()
# 키보드에서 입력받는다.
# 입력받은 값은 공간에 저장하여야 한다.
# input함수를 통하여 입력받은 데이터를 문자열로 변환한다. # 입력 받는 데이터가 무조건 문자열로 변환 된다!!!
# 즉, input함수를 통하여 입력받은 데이터를 내가 원하는 데이터로 형변환을 해주어야한다.

# 형식
# 변수명 = 내가 바꿀 자료형(input("출력하고자하는 내용"))

name = input("이름 입력 :")
age = int(input("나이 입력 :"))
print("이름 : {}".format(name))
print("나이 : {}".format(age))

print(type(name))
print(type(age))

# 여러개 데이터 입력 받기
a , b = int(input("정수 입력 : ")) , int(input("정수 입력 : "))
print(a,b)

a = int(input("정수 입력 : "))
b = int(input("정수 입력 : "))
