# Challenge 1
# Ask the user for a number and a length.
# Create a program that prints a list of multiples of the number until the list length reaches length.

# number=int(input('Pick a number:'))
# leng=int(input('Pick a length:'))
# xxx=[]
# x=1
# while len(xxx)<leng:
#     xxx.append(number*x)
#     x +=1
# print(xxx)


# Challenge 2
# Write a program that asks a string to the user, and display a new string with any duplicate consecutive letters removed.

str1=input("Write a string:")
list1=[]
for i in str1:
    if not list1 or i !=list1[-1]:
        list1.append(i)
result=''.join(list1)
print(result)