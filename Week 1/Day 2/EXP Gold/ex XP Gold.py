#Exercise 1: Concatenate lists
# list1=[1,2,3,4]
# list2=[5,6,7,8]
# list1.extend(list2)
# print(list1)

#Exercise 2: Range of numbers
# for num in range(1500,2501):
#     if num%5==0 or num%7==0:
#         print(num)


#Exercise 3: Check the index
# names = ['Samus', 'Cortana', 'V', 'Link', 'Mario', 'Cortana', 'Samus']
# user_name=input('Whats your name?:')
# for name in names:
#     if user_name==name:
#         print(names.index(name))
    

#Exercise 4: Greatest Number
# numbers=[]
# numbers.append(int(input('Pick 1st number:')))
# numbers.append(int(input('Pick 2nd number:')))
# numbers.append(int(input('Pick 3rd number:')))

# print(max(numbers))


#Exercise 5: The Alphabet
# import string
# string_of_letters=list(string.ascii_lowercase)
# for char in string_of_letters:
#     if char in "aeiou":
#         print(f'{char} is a vowel')
#     else:
#         print(f'{char} is a consonant')


#Exercise 6: Words and letters
# words=[]
# for word in range(7):
#     user_words=input(f'Print word {word+1}:')
#     words.append(user_words)

# # print(words)

# letter=input('Print a single charcter:')
# if len(letter) !=1:
#     print('Enter only 1 character:')
# else:
#     for word2 in words:
#         if letter in word2:
#             print(f'{letter} 1st appears in {word2} at index {word2.index(letter)}')
#         else:
#             print(f'{letter} is not in the {word2}')


#Exercise 7: Min, Max, Sum
# list_numbers=list(range(1,1000001))
# print(min(list_numbers))
# print(max(list_numbers))
# million=sum(list_numbers)
# print(million)


#Exercise 8 : List and Tuple
# numbers=input('Pick some numbers:')
# list1=numbers.split(',')
# tuple1=tuple(list1)

# print(list1)
# print(tuple1)

#Exercise 9 : Random number
import random
correct=0
incorrect=0
while True:
    user_numbers=(input('Pick a number from 1 to 9, or type q:'))
    if user_numbers=='q':
        break
    random_num=random.randint(1,9)
    if user_numbers==random_num:
        correct+=1
        print('Correct')
    else:
        incorrect+=1
        print('No')

print(f'right guesses: {correct}')
print(f'incorrect guesses: {incorrect}')



