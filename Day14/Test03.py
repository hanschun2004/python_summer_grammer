# [문제 3]
'''
message = ['spam', 'ham', 'spam', 'ham','spam']

# A형
dummy = []
for i in message:
    if i == 'spam':
        dummy.append(1)
    elif i == 'ham':
        dummy.append(0)
print(dummy)

# B형       
spam_list = []
for i in message:
    if i == 'spam':
        spam_list.append(i)
print(spam_list)

'''
