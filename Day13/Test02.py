dic = {"과일":['포도','딸기'] , "숫자": 0 ,"문자":"A"}

print(dic)
print(type(dic))


print(dic["과일"]) # key값을 통해 value값을 불러온다.
print(dic["과일"][1])
print(dic["문자"])

for i in dic: # i에는 key값만 담긴다. i ="과일" , "숫자" , "문자"
    print(i , "-", dic[i]) # dic[key]
    








































