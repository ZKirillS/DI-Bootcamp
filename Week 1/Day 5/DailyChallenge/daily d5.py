# Challenge 1 : Sorting
# Write a program that accepts a comma separated sequence of words as input and prints the words in a comma-separated sequence after sorting them alphabetically.
# Use List Comprehension
# Example:

# Suppose the following input is supplied to the program: without,hello,bag,world
# Then, the output should be: bag,hello,without,world

# user_s=input('Print a sequense, separate with comma:')

# sequence=",".join(sorted([char for char in user_s.split(',')]))

# print(sequence)


#Challenge 2 : Longest Word

# Write a function that finds the longest word in a sentence. If two or more words are found, return the first longest word.
# Characters such as apostrophe, comma, period count as part of the word (e.g. O’Connor is 8 characters long).

def longest_word(inputs):
    words = inputs.split()
    longest = words[0]
    for word in words: #for char in words len<
        if len(word)>len(longest):
            longest=word
    return longest #return

print(longest_word("Margaret's toy is a pretty doll."))
print(longest_word("A thing of beauty is a joy forever."))
print(longest_word("Forgetfulness is by all means powerless!"))