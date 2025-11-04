def star(): # 안받고 안주고
    print("★★★★★")

star()
star()
star()

def star(a): # 받고 안주고
    print("★"*a)

star(1)
star(3)

def hello(): # 안반고 주고 () -> 주는 값이 읎다
    return "Python"
a = hello()
print(a)