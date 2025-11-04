tp = 1,2,3,4,5 # packing - () 생략
print(tp)
print(type(tp))

for i in tp:
   print(i) 

print(tp[0])
print(tp[1:3])

# tp[0] = 1  - 값 변경 불가능***
# TypeError: 'tuple' object does not support item assignment

tp = ((1,2),
      (1,2,3),
      (1,2))

print(tp)
print(tp[0]) # tp[0] -0은 세로 인덱스 : (1,2) 
print(tp[0][1]) # tp[0][1] - 세로:0 , 가로 :1 -> 2
print(tp[1][2]) # tp[1][2] - 세로:1 , 가로 :2 -> 3
print(tp[2][0]) # tp[2][0] - 세로:2 , 가로 :0 -> 1
# [세로 인데스] [가로 인데스]
# 튜플명[세로 인덱스][가로 인덱스]

for i in tp: # i = (1,2) , i =(1,2,3) , i =(1,2)
    print(i)
    for j in i: # j=1,2 / j = 1,2,3 / j = 1,2
        print(j)

for i in range(len(tp)):
    for j in range(len(tp[i])):
        print(tp[i][j], end="\t")
    print()


tp = 1,2,3,4,5 # packing
a,b,c,d,e = tp # unpacking
print(a,b,c,d,e)





























