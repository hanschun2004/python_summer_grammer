# 다음에 변수에 저장되어 있는 값을 활용하여 동일한 결과가 나오도록 하세요/.
x , y, z = '100', 10.5, 20

# 110.5
print(float(x)+y)

# 10020
print(str(x)+str(z))

#10.520.0
print(str(y)+str(float(z)))

#110.520
print(str((float(x)+y))+str(z))
