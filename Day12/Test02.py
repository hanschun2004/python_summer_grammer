ls = [1,2,3,4]

print(ls)
# ls[4] = 5 - index가 없기 때문에 error
ls.append(5)
print(ls)

# ls.append((6,7)) - 데이터의 집합 형태 그래도 추가된다.
# print(ls)
ls.extend((6,7))
print(ls)

ls.insert(0,0)
ls.insert(10,8) #존재하지 않는 인덱스여도 마지막 인덱스에 데이터가 추가된다. 
print(ls) 

print(ls.pop(0))
print(ls)
ls.pop() # 인덱스를 적지 않으면 가장 마자막 데이터가 잘라내기 된다.
print(ls)

ls.remove(7) # 값 삭제
print(ls)
 
ls.clear()
print(ls)


ls = [9,1,5,3,7,8,2,4,6]
print(ls)
ls.reverse()
print(ls)
ls.sort() # 오름차순
print(ls)
ls.sort(reverse = True)
print(ls)
























