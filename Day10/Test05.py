# 구구단
# ===== 2단 =====
# 2 x 1 = 2
# 2 x 2 = 4
# ...
# 2 x 9 = 18
# ===== 3단 =====
# 3 x 1 = 3
# ...

for i in range(2,10):
    print("===== {}단 =====".format(i))
    for j in range(1,10):
        print("{} x {} = {}".format(i,j,i*j))
    print("="*15)










