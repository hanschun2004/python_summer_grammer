# 책 79p 4번
# 중첩 반복문을 이용한 단어 카운트 하기
multiline ="""안녕하세요. 파이썬 세계로 오신걸
환영합니다.
파이썬은 비단뱀 처럼 매력적인 언어입니다."""

# <출력 결과>
# 안녕하세요.
# 파이썬
# 세계로
# 오신걸
# 환영합니다
# 파이썬은
# 비단뱀
# 처럼
# 매력적인
# 언어입니다.
# 단어 개수 : 10


multiline ="""안녕하세요. 파이썬 세계로 오신걸
환영합니다.
파이썬은 비단뱀 처럼 매력적인 언어입니다."""

'''
List = multiline.split("\n")
tot = 0
for i in range(0, len(List)):
    line = List[i].split(" ")
    tot += len(line)
    for j in range(0,len(line)):
        print(line[j])
        
print("단어 개수 : {}".format(tot))    
'''

cnt = 0
for i in multiline.split("\n"):
    for j in i.split(" "):
        cnt += 1
        print(j)
print("단어개수 : {}".format(cnt))


















































