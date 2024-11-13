# Exercise 1 – Random Sentence Generator
# import random

# def get_word_from_file():
#     with open("C:\\Users\\chekf\\OneDrive\\Документы\\Vis DI-BOOTCAMP\\Week 2\\day 4\\sowpods.txt",'r+',encoding='utf-8') as f:
#         content = f.read().splitlines() # this function reading the file content and saving it into a readable list
#     return content # returning a list of words from a file

# def get_random_sentence(words,lenght):
#     random_sentence = random.sample(words,lenght)
#     return ' '.join(random_sentence)

# def main():
#     print('This programm generating a random sentence for users input lenght')
#     try:
#         user_lenght = int(input('How long you want the sentence to be?'
#                             'Print a number between 2 and 20:'))
#         if 2<=user_lenght<=20:
#             words = get_word_from_file()
#             sentence = get_random_sentence(words,user_lenght).lower()
#             print(sentence)
#         else:
#             raise ValueError('Incorrect data, you need to pick a number between 2 and 20')

#     except ValueError as e:
#         print(f'Error: {e}')

# if __name__ == '__main__':
#     main()


# Exercise 2: Working with JSON

import json
sampleJson = """{ 
   "company":{ 
      "employee":{ 
         "name":"emma",
         "payable":{ 
            "salary":7000,
            "bonus":800
         }
      }
   }
}"""


data =json.loads(sampleJson)

salary = data["company"]["employee"]["payable"]["salary"]
print(salary)
data["company"]["employee"]["birth_date"] = "1995/10/04"
print(data)

with open("sampleJson.json","w") as json_file:
    json.dump(data,json_file,indent=2,sort_keys=True)

