# Now create another Python file, called anagrams.py. 
# This will contain all the UI (user interface) functionality 
# of your program and will rely on AnagramChecker
# for the anagram-related logic.

from anagram_checker import AnagramChecker

def menu():
    print('***************************')
    print('Welcome to ANAGRAM CHECKER')
    print('***************************')
    print('[1] Input a word')
    print('[0] Exit')
        


def main():
    
    anagram = AnagramChecker()

    while True:
        menu()
        option = input('Enter your option: ')

        if option == '1':
            user_word = input('Please enter a word: ').strip()

            if len(user_word.split()) != 1:
                print(f'Please enter only 1 word')
            elif not user_word.isalpha():
                print(f'Only alphabetic characters allowed!')
            else:
                if anagram.is_valid_word(user_word):
                    print(anagram.is_valid_word(user_word))
                    user_anagram = anagram.get_anagrams(user_word)
                    if user_anagram:
                        print(f'Anagrams of "{user_word}":{user_anagram}')
                    else:
                        print(f'No anagrams for {user_word} found')
                else:
                    if not anagram.is_valid_word(user_word):
                        print(anagram.is_valid_word(user_word))
        elif option == '0':
            print(f'Goodbay! See you later!')
            break
        else:
            print(f'Invalid option. Print a valid number')
        

if __name__ == "__main__":
    main()