# 모든 제어문은 중첩이 가능하다
# 다중 for문
# - for문 안에 for 문이 있는 형태
# - 중첩적인 구조를 가지는 for문

for i in range(1,3):
    print("{}번째 외부 for문 실행".format(i))
    for j in range(1,4): # i 가 한번 돌떄 j 는 끝값에 도달할 때가지 반복돈다.
        print("내부 for문 실행")
    print("{}번째 외부 for문 종료".format(i))

# i = 1 , j = 1,2,3
# i = 2 , j = 1,2,3

    
