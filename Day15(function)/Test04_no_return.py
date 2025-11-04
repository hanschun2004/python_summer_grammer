# 문제 1) 1부터 5까지 합을 출력하는 함수
def sum1():
	tot = 0
	for i in range(1,6):
		tot += i
	print(tot)

sum1()

# 문제 2) x부터 y까지의 합을 출력하는 함수
def sum2(x,y):
	tot = 0
	for i in range(x,y+1):
		tot += i
	print(tot)

sum2(1,5)

# 문제 3) 정수 3개를 입력받아 최대값을 출력하는 함수
def maxNum():
	maxN=a
	if maxN <b:
		maxN = b
	if maxN < c:
		maxN = c
	print(maxN)

a = int(input("a 입력 : "))
b = int(input("b 입력 : "))
c = int(input("c 입력 : "))
maxNum(a,b,c)

# 문제 4) 리스트 nums를 전달받아 최대값을 출력하는 함수

nums = [10, 87, 23, 19, 3]
def maxNums(ls):
	maxNum = 0
	for i in ls:
		if maxNum < i:
			maxNum = i
	print(maxNum)

maxNums(nums)