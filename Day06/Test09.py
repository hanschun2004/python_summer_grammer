# 국어, 영어, 수학 점수 3개를 입력 받아서 평균이 60점 이상이고
# 각점수가 40점이상이면 합격 아니면 불합격

# 단, 불합격일때 어떤 점수가 부족해서 불합격 인지 출력
# ex) 평균 국어 점수 미달 수학 미달


# my 코드
'''
kor, eng, math = int(input("국어 입력 : ")), int(input("영어 입력 : ")) ,int(input("수학 입력 : ")) 

avg = (kor + eng + math) / 3
if avg >= 60 and kor>=40 and eng>=40 and math >= 40:
    print("합격")

else:
    print("불합격")
    if kor<40:
        print("국어 미달", end=" ")
    if eng<40:
        print("영어 미달", end=" ")
    if math<40:
        print("수학 미달", end=" ")
'''

    


# 정답

kor = int(input("국어 점수 입력 : "))
eng = int(input("영어 점수 입력 : "))
math = int(input("수학 점수 입력 : "))
tot= kor + eng + math
avg = tot / 3

if avg >= 60 and kor >= 40 and eng>=40 and math >= 40:
    print("합격")
else:
    print("불합격")
    if avg < 60:
        print("평균",end=" ")
    if kor < 40:
        print("국어",end=" ")
    if eng < 40:
        print("영어",end=" ")
    if math < 40:
        print("수학",end=" ")
    print("점수 미달")
