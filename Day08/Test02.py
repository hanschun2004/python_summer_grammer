# 다음 조건을 보고 회원가입을 위한
# 프로그램 코드를 작성하세요.
# 아이디는 반드시 10자리 이상
# 패스워드는 반드시 8~16자리 사이
# 패스워드는 아이디가 포함되면 안됨

# 문자열 함수를 응용하여 if

'''
Id = input("아이디 입력 : ")

while len(Id) < 10:
    if len(Id) < 10:
        print("10자리 이상으로 입력 바람")
        Id = input("아이디 입력 : ")
    else:
        break

password = input("비밀번호 입력 : ")

while (len(password)<8 or len(password)>16) or password.find(Id) != -1: 
    if len(password)<8 or len(password)>16:
        print("8~16자리 사이로 입력 바람")
        password = input("비밀번호 입력 : ")
    elif password.find(Id) != -1:
        print("아이디가 패스워드에 포함되면 안됨")
        password = input("비밀번호 입력 : ")
    else:
        break

print("회원 가입 성공!!")
print(Id)
print(password)
'''

user = input("아이디 입력 : ")

if user.__len__() >= 10:
    pw = input("비밀번호 입력 : ")

    if pw.__len__() <8 or len(pw) > 16:
        print("비밀번호는 8자에서 16자 사이어야 합니다.")
    elif pw.find(user) >= 0:
        print("비밀번호는 아이디를 포함시킬 수 없습니다")
    else:
        print("아이디 : {}".foramt(user))
        print("비밀번호 : {}".format(pw))
else:
    print("아이디는 반드시 10자리 이상이어야 합니다.")
    



























        
