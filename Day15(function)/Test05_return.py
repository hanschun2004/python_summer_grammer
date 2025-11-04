nums = [10,20,30,40,50]
# 문제 1) 리스트의 전체합을 리턴해주는 함수
def lsTot(ls):
	tot = 0;
	for i in ls:
		tot += i
	return tot

print(lsTot(nums))
tot = lsTot(nums)
print(tot)

# 문제 2) 4의 배수의 합을 리턴해주는 함수
def flsTot(ls):
	tot = 0
	for i in ls:
		if i%4 == 0:
				tot += i
	return tot
print(flsTot(nums))

# 문제 3) 4의 배수로만 리스트 타입으로 리턴해주는함수
# ex) [20,40]

def fls(ls):
	f = []
	for i in ls:
		if i%4==0:
		    f.append(i)
	return f

print(fls(nums))
ls = fls(nums)
print(ls)