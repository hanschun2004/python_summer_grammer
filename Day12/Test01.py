ls = [ 1, 1.234 , 'a' , "abc" , (1,2) , [1,2,3]]
print(type(ls))
print(ls)

print(ls[5][2])

ls = [1,2,3,4]
a,b,c,d = ls # unpacking 가능
print(a,b,c,d)
# packing 불가능

ls[0] = 0
print(ls)
print()
for i in ls:
    print(i)
print()
for i in range(len(ls)):
    print(ls[i])

    
               
