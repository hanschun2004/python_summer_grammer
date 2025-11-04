# 1 ~ 30 까지 출력
# <출력 결과>
# 1     2       3       4       5
# 6     7       8       9       10
# 11    12      13      14      15
# 16    17      18      19      20
# 21    22      23      24      25
# 26    27      28      29      30

# 다중 반복문
# 세로줄 개수: 외부 반복문의 횟수
# 가로줄 개수: 내부 반복문의 횟수


i = 1
for i in range(1,27,5): # 나는 시작점 5씩 증가시켜주면서 한줄 씩 뽑아내는 방식으로 함
    print(i, end="\t")
    cnt = 1
    for cnt in range(i+1,i+5):
        print(cnt, end="\t")
    print()
    
cnt = 1
for i in range(6): # i를 횟수로만 사용할 수도 있음 
    for j in range(5): # cnt가 총 내부 반복문이 30번이 반복되면서 1씩 증가하였다.
        print(cnt,end="\t")
        cnt += 1
    print()

    
