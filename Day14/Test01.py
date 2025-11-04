# 110p
# [문제 1]

# <출력>
# 단계 1 : [10,1,5,2,10,1,5,2]
# 단계 2 : [10,1,5,2,10,1,5,2,20]
# 단계 3 : [1,2,1,2]
'''
ls = [10,1,5,2]

result = ls*2
print(result)

a = result[0]*2
result.append(a)
print(result)


result2 = []
for i in range(len(result)-1):
    if i % 2 != 0:
        result2.append(result[i])
print(result2)
'''

'''
lst = [10,1,5,2]
result = []
'''
# 단계 1
'''
result = []
for i in range(len(lst)):
    result.append(lst[i])
for i in range(len(lst)):
    result.append(lst[i])
print(result)


for i in range(4):
    lst.append(lst[i])
for i in lst:
    result.append(i)
print(result)
'''
'''
result = lst *2
print(result)
# 단계 2
result.append(lst[0] * 2)
print(result)

# 단계 3
result2 = []
for i in range(len(result)): # 0 ~ 8
    if i % 2 == 1:
        result2.append(result[i])
print(result2)      
    
'''
