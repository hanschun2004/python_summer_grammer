def test(a,b,c):
    if a < b:
        return b, c
    if a > b:
        return a , c

n1, n2 = test(1,2,"크다")
print(n1,n2)

def test1():
    return [1,2], (1,2) # 리턴값이 여러개면 튜플 형태로 묶어서 return한다.

print(test1())