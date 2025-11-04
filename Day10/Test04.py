# 책 79p
# for 반복문을 이용한 수열 출력하기
# 1 ~ 100 사이에서 3의 배수이면서 2의배수가 아닌 수를 한줄에 출력하고, 누적합을 출력

# <출력 결과>
# 수열 = 3 9 15 21 27 33 39 45 51 57 63 69 75 81 87 93 99
# 누적합 = 867

tot = 0
print("수열 = ", end="")
for i in range(1,101):
    if i % 3 == 0 and i % 2 != 0:
        print(i,end=" ")
        tot += i
print("\n누적합 = {}".format(tot))
print()
print("누적합 = {}".format(tot))





























