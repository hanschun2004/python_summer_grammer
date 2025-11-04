#파이썬에서는 함수의 옵션이 존재
#end
# 출력할때 가장 끝에 자동으로 삽입되는 문자를 지정하는 옵션
# 디폴트값으로 \n 으로 지정되어 있다.
print("hello python", end="\n")
print("안녕하세요", end='\n') #디폴트값
print("Hello Python",end=" ")
print("안녕하세요")


print(1, end = " , ")
print(2, end = " , ")
print(3)

#sep
# 데이터들을 출력할때 중간중간 삽입되는 문자를 지정하는 옵션
# 디폴트값으로 space 로 지정되어 있다.
print(1,2,3,4,5)
print(1,2,3,4,5,sep=" ") # 디폴트값
print(1,2,3,4,5,sep="*")
print(1,2,3, sep="+", end ="=")
print(6)

