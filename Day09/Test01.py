# 구구단 게임
# 1. 구구단 게임을 사용자가 3번 틀리기 전까지 반복
# 2. 사용자가 정답을 맞추면 20점 증가 , 정답개수 1 증가
# 3. 사용자가 정답을 틀리면 5점 감점 , 틀린개수 1 증가
# 4. 게임 종료 후 성적을 출력

# 1. 무한 반복을 돌린다.
# 2. 랜덤 2개 - 단(2~9) , 곱해지는 수(1~9) ex) 3 1 
# 3. 사용자에게 랜덤 값 두개를 출력 ex) 3 X 1 =
# 4. 사용자가 정답을 입력 ex) 3
# 5. 사용자가 입력한 정답과 두개의 곱한 값이 동일한지
# 5-1. 동일하면 score에 20점을 누적, cnt 1의 값을 1 증가
# 5-2. 동일하지 않으면 score 값을 5점 감소, cnt2의 값을 1증가
# 6. cnt2의 값이 3이 되면 반복문 종류 (break)
'''
import random
life = 3
correct = 0
wrong = 0
score = 0
print("구구단 게임")
while life >= 1:
    first = int(random.random()*9) + 1
    second = int(random.random()*9) +1
    answer = first * second
    user = int(input("{} X {} = ".format(first,second)))
    if user == answer:
        print("정답!")
        correct += 1
    else:
        print("오답")
        wrong += 1
        life -= 1

score = 20 * correct - 5 * wrong
print("점수 : {} , 맞은 개수 : {} , 틀린 개수 : {}".format(score, correct, wrong))

'''
import random
score = 0 # 점수
cnt1 = 0 # 정답 개수
cnt2 = 0 # 틀린 개수

while True:
    a = int(random.random() * 8) + 2
    b = int(random.random() * 9) + 1

    # print("{} x {} = ".format(a , b), end ="")
    user = int(input("{} x {} = ".format(a,b)))
    if user == a*b:
        print("정답 !")
        score += 20
        cnt1 +=1
    else:
        print("오답 !")
        score -=5
        cnt2 += 1    
        if cnt2 == 0:
            print("정답 개수 : {}개 , 총 점수 : {}점".format(cnt1, score))
            break
    
            



































