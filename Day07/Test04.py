# 영문자를 입력 받아 대, 소 문자를 구분한뒤
# 소문자는 대문자로 대문자는 소문자로
# 특수문자 및 숫자를 입력할 시 잘못된 입력이라는 문구 표시


ch = input("영문자 입력 : ")[0] # h = ch[0]  "asjdsfa" -> "a"

if ch >= 'a' and ch <= 'z':
    print("{}의 대문자 : {}".format(ch,chr(ord(ch)-32)))
elif ord(ch) >= 65 and ord(ch)<=90:
    print("{}의 소문자 : {}".format(ch,ch+32))
else:
    print("잘못된 입력 !")

ch = ord(input("영문자 입력 : ")[0])

if 97 <= ch <= 122:
    print("{}의 대문자 : {}".format(chr(ch),chr(ch-32)))
elif 65 <= ch <= 90:
    print("{}의 소문자 : {}".format(chr(ch),chrch+32))
else:
    print("잘못된 입력 !")


'''    
alpa = input("영문자 입력 : ")
num = ord(alpa[0])

if 90 >= num >= 65:
    print(chr(num+32))
    
    
elif 97 <= num <= 122:
    print(chr(num-32))
else:
    print("잘못된 입력")



#65~90
#97~122

'''


