# 책 p57쪽
# 문제 4
'''
word1 = input("첫번째 단어 : ")[0]
word2 = input("두번째 단어 : ")[0]
word3 = input("세번째 단어 : ")[0]
abbr = ""
abbr = word1 + word2 + word3
print("="*15)
print("약자 : {}".format(abbr))
'''

word1 = input("첫번째 단어 : ")
word2 = input("두번째 단어 : ")
word3 = input("세번째 단어 : ")
print("="*15)
abbr = word1[0] + word2[0] + word3[0]
print("약자 : {}".format(abbr))


# 문제 4-1
# 3개의 단어를 입력받고
# 한개의 단어에서 랜덤적으로 문자 하나 추출 후
# 3개의 단어에서 랜덤 추출된 문자를 합쳐서 출력
'''
import random

word1 = input("첫번째 단어 : ")
word2 = input("두번째 단어 : ")
word3 = input("세번째 단어 : ")
idx1= int(random.random() * word1.__len__())

rand1 = random.randint(0, len(word1)-1)
rand2 = random.randint(0, len(word2)-1)
rand3 = random.randint(0, len(word3)-1)

abbr = word1[rand1] + word2[rand2] + word3[rand3]
print("약자 : {}".format(abbr))
'''

import random
word1 = input("첫번째 단어 : ")
word2 = input("두번째 단어 : ")
word3 = input("세번째 단어 : ")

idx1= int(random.random() * word1.__len__())
idx2= int(random.random() * word2.__len__())
idx3= int(random.random() * len(word3))

abbr = word1[idx1] + word2[idx2] + word3[idx1]
print("문자열 : {}".format(abbr))









