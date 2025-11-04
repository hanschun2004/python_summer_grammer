dic = {'a' : 1 , 'b' : 2 , 'c' : 3}

# Dictionary(사전형)에서 사용되는 함수

# update(dict)
# - 사전형 자료에 값을 추가한다.
# - key 값이 같으면 value값을 업데이트하고.. key 값이 없으면 추가
dic.update({'a' : 4 , 'd' : 5})
print(dic)

# fromkeys(iter,value)
# - 리스트, 튜플에 존재하는 값을 키로 사전형 자료를 생성하여 반환한다.
# - value 값은 일괄적으로 설정될 수 밖에 없다.
# 이터레이터 :  iterator란 반복 가능한 객체(리스트, 퓨플, 셋, 사전, 문자열)에서
# 반복문을 활용하여 데이터를 순회하면서
# 각 요소를 하나씩 꺼내 어떤 처리를 수행할 수 있도록 하는 간편한 방법을 제공하는 객체이다.

ls = [1,2,3,4]
print(dic.fromkeys(ls,"hi"))

# get(key , [value])
# 사전형의 키를 통해 값을 반환한다.
# - key 값이 없으면 None 을 반환한다.
# - key 값이 있으면 value 값을 반환한다.

print(dic.get('a'))
print(dic.get('e') == None)
print(dic.get('e',1)) # 임식적으로 value값을 설정하여 None 이 나오지 않게...

# keys()
# 사전형의 모든 키를 반환한다.
# 리스트나 튜플 타입으로 변환하여 사용 가능
key = dic.keys()
print(list(key))

# values()
# 사전형의 모든값을 반환한다.
# 리스트나 튜플타입으로 변환하여 사용가능하다.
# 사전형의 모토가 벗어나므로 잘 사용되지 않는다.**
print(dic.values())

# items()
# 사전형의 모든 key - value 의 쌍을 튜플로 반환한다.
# 리스트나 튜플타입으로 변환하여 사용 가능하다.
tp = dic.items()
print(tuple(tp))
print(list(tp)[2][1]) # list(tp)[2] -> ('c',3)[1] -> 3

# pop(key)
# 사전형의 키를 통해 값을 반환 후 삭제한다.
# key값이 없으면 error 발생
print(dic.pop('a'))
print(dic)

# popitem()
# 사전형의 key - value 의 쌍으로 튜플로 반환 후 삭제한다.
# 제일 끝에 있는 데이터부터 삭제시킨다.
print(dic.popitem())
print(dic)

# clear()
# 사전형의 모든 키값을 삭제하여 빈 사전형 자료형만 남는다.
dic.clear()
print(dic)













































