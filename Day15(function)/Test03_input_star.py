# 숫자를 입력 받고 그 입력 받은 숫자 만큼 별을 출력하세요(단, 문자열 연산 사용 x , 반복문 O)
def star(su):
	st= ""
	for i in range(su):
		st += "★"
	return st

su = int(input("별의 개수 : "))
st = star(su)
print(st)
su = int(input("별의 개수 : "))
print(star(su))