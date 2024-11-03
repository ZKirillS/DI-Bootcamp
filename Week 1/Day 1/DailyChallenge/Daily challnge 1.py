st1=str(input('Print a string 10 chr long:'))
if len(st1)<10:
    print("string not long enough")
elif len(st1)>10:
    print("string too long")
else:
    print("perfect string")
print(st1[0])
print(st1[-1])

for i in range(len(st1)):
    print(st1[:i+1])


import random
a=list(st1)
random.shuffle(a)
print(''.join(a))