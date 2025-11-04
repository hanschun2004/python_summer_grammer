# 학생 이름 / 국어 / 영어 / 수학 점수를 입력 받아서 출력

# <입력>
# 학생 이름 : 개똥이
# 국어 점수 : 80
# 영어 점수 : 80
# 수학 점수 : 80

# <출력>
# ==============학생 정보======================
# 이름    국어      영어    수학    합계     평균
# 개똥이   80       80     80      240    80.0

# name = input("학생 이름을 입력하세요 : ")
# korean = int("국어 점수를 입력하세요 : ")
# english = int("영어 점수를 입력하세요 : ")
# math = int("수학 점수를 입력하세요 : ")
# sumall = korean + english + math
# average = sumall / 3

# print("="*13, end = "=")
# print("{}".format("학생 정보"), end = "=")
# print("="*13)

# print("{:<4}{:^5}{:^5}{:^5}{:^5}{:>4}".format("이름", "국어", "영어", "수학", "합계", "평균"), sep= " ")
# print("{:<4}{:^5}{:^5}{:^5}{:^5}{:>4}".format(name, korean, english, math, sumall, average), sep= " ")


name = input("학생 이름 : ")
kor = int(input("국어 점수 : "))
eng = int(input("영어 점수 : "))
math = int(input("수학 점수 : "))
tot = kor + eng + math
avg = tot/3
print("="*18, "학생 정보", "="*18)
print("이름\t국어\t영어\t수학\t합계\t평균")
print("{}\t{}\t{}\t{}\t{}\t{:.1f}".format(name, kor, eng, math, tot, avg))
print("{:6}{:<8}{:<8}{:<8}{:<8}{:<8.1f}".format(name, kor, eng, math, tot, avg))

