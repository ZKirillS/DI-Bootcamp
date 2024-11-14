# Anagram checker

class AnagramChecker:
    def __init__(self,file="C:\\Users\\chekf\\OneDrive\\Документы\\Vis DI-BOOTCAMP\\Week 2\\day 5\\sowpods.txt"):
        self.text = set()
        try:
            with open(file,'r+',encoding='utf-8') as f:
                for line in f:
                    word = line.strip().lower()
                    if word:
                        self.text.add(word)
        except FileNotFoundError:
            return 'Error: File not found'

    def is_valid_word(self,word):
        if word.lower() in self.text:
            return f'{word} is a valid English word'
        else:
            return f'{word} is not valid English word'

    def get_anagrams(self,word):
        words_sort = sorted(word.lower())
        list_of_anagrams = [char for char in self.text if sorted(char) == words_sort and char != word.lower()]
        return list_of_anagrams



anagram = AnagramChecker()
# print(anagram.is_valid_word('Hello'))
# print(anagram.is_valid_word('Popopap'))
# anag1 = anagram.get_anagrams('meat')
# anag2 = anagram.get_anagrams('stub')
# print(anag2)
# print(anag1)