# *
# **
# ***
# ****
# *****

# *****
# ****
# ***
# **
# *

#     *
#    **
#   ***
#  ****
# *****

#     *
#    ***
#   *****
#  *******
# *********

# 외부 반복문 세로줄의 개수
# 내부 반복문 가로줄의 개수

'''
for i in range(1,6):
    print("*"*i)

for i in range(1,6):
    print("*"*(6-i))


for i in range(1,6):
    print(" "*(6-i),end ="")
    print("*"*i)
'''
    
for i in range(1,6):
    for j in range(0,i,1):
        print("*",end="")
    print() # i = 1 j = 0 / i =2 j = 0,1 / i = 3

print()

for i in range(1,6):
    for j in range(6,i,-1):
        print("*",end="")
    print() # i = 1 j = 6,5,4,3,2 / i = 2 j = 6,5,4,3 / ..

for i in range(1,6):
    for j in range(5,i,-1):
        print(" ",end="")
    for k in range(0,i):
        print("*",end="")
    print() # i =1 j =5,4,3,2 k = 0 / i=2 j=5,4,3 k =0,1 / ..

print()

# 계산식 이용
for i in range(1,6):
    for j in range(5,i,-1):
        print(" ",end="")
    for k in range(0,i*2-1):
        print("*",end="")
    print()

# 변수 이용
n= 1
for i in range(1,6):
    for j in range(5,i,-1):
        print(" ",end="")
    for k in range(0,n):
        print("*",end="")
    print()
    n+=2
    























































