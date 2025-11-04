# 이름, 학번, 3과목 성적을 입력 받아 초범과 평균을 구하고
# 평균이 90점이상이면 'A' 80점이상이면 'B' 70점이상이면 'C'
# 60점이상이면 'D' 그외 'F'

name = input("이름 입력 : ")
stu_num = int(input("학번 입력 : "))
lecture1 = int(input("과목 1 성적 입력 : "))
lecture2 = int(input("과목 2 성적 입력 : "))
lecture3 = int(input("과목 3 성적 입력 : "))
grade = " "
tot = lecture1 + lecture2 + lecture3
avg = tot/3

if avg >= 90:
    grade = 'A'
elif avg>= 80:
    grade = 'B'
elif avg>= 70:
    grade = 'C'
elif avg>= 60:
    grade = 'D'
else:
    grade = 'F'

print()
print("이름\t학번\t총점\t평균\t등급")
print("{}\t{}\t{}\t{:.2f}\t{}".format(name, stu_num, tot, avg, grade))



