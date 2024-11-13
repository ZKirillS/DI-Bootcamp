# Daily challenge : Text Analysis
# The goal of the exercise is to create a class that will help you 
# analyze a specific text. A text can be just a simple string, 
# like “Today, is a happy day” or it can be an external text file.

from collections import Counter
import string
import spacy

class Text():
    def __init__(self,text):
        self.text = text
    
    def get_text(self):
        return self.text
    
    def frequency(self,word):
        words = self.text.split()
        count = words.count(word)
        if count > 0:
            return f'{word} - {count}'
        else:
            return f'{word} is not found'

    def common(self):
        words = self.text.split()
        word_count = Counter(words)
        most_common = word_count.most_common(-1)
        if most_common:
            return most_common[0]
        else:
            return 'No words found'

    def unique(self):
        words = self.text.split()
        unique_words = set(words)

        return sorted(list(unique_words))

    @classmethod
    def get_text_from_file(cls,name):
        try:
            with open(name,'r+',encoding='utf-8') as f:
                content = f.read()
            return cls(content)
        except FileNotFoundError:
            return f'File is not found'

    @classmethod
    def without_punctuation(self):
        text_to_check = str.maketrans('','',string.punctuation)
        clean_text = self.text.translate(text_to_check)
        return clean_text

    @classmethod
    def stop_words(self):
        nlp = spacy.load("en_core_web_sm")
        doc = nlp(self.text)
        filtered_words = [token.text for token in doc if not token.is_stop]
        clean_text = ' '.join(filtered_words)
        return clean_text

    @classmethod
    def specials(self):
        special_sign = [';', ':', '!', "*", " ",",",".","?","'",".,","-","(",")","♦",'"',"—"]
        self.text = ''.join(i for i in self.text if not i in special_sign)
        return self.text


class TextModification(Text):
    def __init__(self, text):
        super().__init__(text)
    
    def without_punctuation(self):
        text_to_check = str.maketrans('','',string.punctuation)
        clean_text = self.text.translate(text_to_check)
        return clean_text

    def stop_words(self):
        nlp = spacy.load("en_core_web_sm")
        doc = nlp(self.text)
        filtered_words = [token.text for token in doc if not token.is_stop]
        clean_text = ' '.join(filtered_words)
        return clean_text

    def specials(self):
        special_sign = [';', ':', '!', "*", " ",",",".","?","'",".,","-","(",")","♦",'"',"—"]
        self.text = ''.join(i for i in self.text if not i in special_sign)
        return self.text



# simple_string = Text('A good book would sometimes cost as much as a good house')
# print(simple_string.get_text())
# uniques = simple_string.unique()
# print(uniques)
# common_w = simple_string.common()
# print(common_w)
# print(simple_string.frequency('book'))
my_text_path = Text.get_text_from_file('C:\\Users\\chekf\\OneDrive\\Документы\\Vis DI-BOOTCAMP\\Week 2\\day 4\\the_stranger.txt')
# common_t = my_text_path.unique()
# print(common_t)
# common_f = my_text_path.without_punctuation()
# print(common_f)
# clean_t = my_text_path.stop_words()
# print(clean_t)
# clean_s = my_text_path.specials()
# print(clean_s)
my_text_path2 = TextModification.get_text_from_file('C:\\Users\\chekf\\OneDrive\\Документы\\Vis DI-BOOTCAMP\\Week 2\\day 4\\the_stranger.txt')
clean_s = my_text_path2.specials()
print(clean_s)
