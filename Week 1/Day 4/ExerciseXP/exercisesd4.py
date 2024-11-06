#Exercise 1 : What are you learning ?
# Write a function called display_message() that prints one sentence telling everyone what you are learning in this course.
# Call the function, and make sure the message displays correctly.

# def display_message():
#     print('Im learning functions in this course')
# display_message()

# Exercise 2: What’s your favorite book ?
# Write a function called favorite_book() that accepts one parameter called title.
# The function should print a message, such as "One of my favorite books is <title>".
# For example: “One of my favorite books is Alice in Wonderland”
# Call the function, make sure to include a book title as an argument when calling the function.

# def favorite_book(title):
#     print(f'One of my favorite books is {title}')

# favorite_book('Alice in Wonderland')


# Exercise 3 : Some Geography
# Write a function called describe_city() that accepts the name of a city and its country as parameters.
# The function should print a simple sentence, such as "<city> is in <country>".
# For example “Reykjavik is in Iceland”
# Give the country parameter a default value.
# Call your function.

# def describe_city(city='',country=''):
#     city=input('What is your city?')
#     country=input('What is your country?')
#     print(f'{city} is in {country}')

# describe_city()


# Exercise 4 : Random
# Create a function that accepts a number between 1 and 100 and generates another number randomly between 1 and 100. Use the random module.
# Compare the two numbers, if it’s the same number, display a success message, otherwise show a fail message and display both numbers.

# import random

# def random_numbers(number=''):
#     number=int(input('Pick a number:'))
#     for number in range(1,101):
#         print(random.randrange(101))
#         break

# random_numbers()

#Exercise 5 : Let’s create some personalized shirts !
# Write a function called make_shirt() that accepts a size and the text of a message that should be printed on the shirt.
# The function should print a sentence summarizing the size of the shirt and the message printed on it, such as "The size of the shirt is <size> and the text is <text>"
# Call the function make_shirt().
# Modify the make_shirt() function so that shirts are large by default with a message that reads “I love Python” by default.
# Call the function, in order to make a large shirt with the default message
# Make medium shirt with the default message
# Make a shirt of any size with a different message.
# Bonus: Call the function make_shirt() using keyword arguments.

# def make_shirt(size='large',text='I love Python'):
#     text=input('Write your text:')
#     size=int(input('Pick your size:'))

#     print(f'The size of the shirt is {size} and the text is {text}')

# make_shirt()

# def make_shirt(size='large',text='I love Python'):
#     print(f'The size of the shirt is {size} and the text is {text}')

# make_shirt()


# def make_shirt(size='medium',text='I love Python'):
#     print(f'The size of the shirt is {size} and the text is {text}')

# make_shirt()


# def make_shirt(size='small',text='I love Developers Institute'):
#     print(f'The size of the shirt is {size} and the text is {text}')

# make_shirt()


# def make_shirt(**kwargs):
#     print('The size of your shirt:')
#     for key,value in kwargs.items():
#         print(key + ' ' +value)


# make_shirt(size='medium',text='how it still working')


# Exercise 6 : Magicians …
# Using this list of magician’s names

# magician_names = ['Harry Houdini', 'David Blaine', 'Criss Angel']

# # Create a function called show_magicians(), which prints the name of each magician in the list.
# # Write a function called make_great() that modifies the original list of magicians by adding the phrase "the Great" to each magician’s name.
# # Call the function make_great().
# # Call the function show_magicians() to see that the list has actually been modified.

# def show_magicians():
#     for name in magician_names:
#         print(name)



# def make_great():
#     global magician_names
#     magician_names=[name+' the Great' for name in magician_names]

# make_great()
# show_magicians()


# Exercise 7 : Temperature Advice
# Create a function called get_random_temp().
# This function should return an integer between -10 and 40 degrees (Celsius), selected at random.
# Test your function to make sure it generates expected results.

# import random
# def get_random_temp(season=''):
#     if season=='winter':
#         return(float(random.randrange(-10,0)))
#     elif season=='autumn':
#         return(float(random.randrange(0,16)))
#     elif season=='spring':
#         return(float(random.randrange(16,28)))
#     elif season=='summer':
#         return(float(random.randrange(28,41)))
    

# def main():
#     month=int(input(f'Please select a month number:'))
#     if 3<=month<=5:
#         season='spring'
#     elif 6<=month<=8:
#         season='summer'
#     elif 9<=month<=11:
#         season='autumn'
#     elif month==1 or month==2 or month==12:
#         season='winter'
    
#     new_temperature = get_random_temp(season)
#     print(f'The temperature right now is {new_temperature} degrees Celsius.')
#     if new_temperature<0:
#         print('Brrr, thats freezing! Wear some extra layers today')
#     elif 0<=new_temperature<16:
#         print('Quite chilly! Dont forget your coat')
#     elif 16<new_temperature<=23:
#         print('Awesome weather for a walk')
#     elif 24<=new_temperature<=32:
#         print('You should go to the sea!')
#     elif 33<=new_temperature<=40:
#         print('Quite hot! Dont go for a walk')

# main()

# Create a function called main().
# Inside this function, call get_random_temp() to get a temperature, and store its value in a variable.
# Inform the user of the temperature in a friendly message, eg. “The temperature right now is 32 degrees Celsius.”

# Let’s add more functionality to the main() function. Write some friendly advice relating to the temperature:
# below zero (eg. “Brrr, that’s freezing! Wear some extra layers today”)
# between zero and 16 (eg. “Quite chilly! Don’t forget your coat”)
# between 16 and 23
# between 24 and 32
# between 32 and 40

# Change the get_random_temp() function:
# Add a parameter to the function, named ‘season’.
# Inside the function, instead of simply generating a random number between -10 and 40, set lower and upper limits based on the season, eg. if season is ‘winter’, temperatures should only fall between -10 and 16.
# Now that we’ve changed get_random_temp(), let’s change the main() function:
# Before calling get_random_temp(), we will need to decide on a season, so that we can call the function correctly. Ask the user to type in a season - ‘summer’, ‘autumn’ (you can use ‘fall’ if you prefer), ‘winter’, or ‘spring’.
# Use the season as an argument when calling get_random_temp().

# Bonus: Give the temperature as a floating-point number instead of an integer.
# Bonus: Instead of asking for the season, ask the user for the number of the month (1 = January, 12 = December). Determine the season according to the month.


#Exercise 8 : Star Wars Quiz
# This project allows users to take a quiz to test their Star Wars knowledge.
# The number of correct/incorrect answers are tracked and the user receives different messages depending on how well they did on the quiz.
# Here is an array of dictionaries, containing those questions and answers

data = [{"question": "What is Baby Yoda's real name?",
         "answer": "Grogu"},
    {"question": "Where did Obi-Wan take Luke after his birth?",
        "answer": "Tatooine"},
    {"question": "What year did the first Star Wars movie come out?",
        "answer": "1977"},
    {"question": "Who built C-3PO?",
        "answer": "Anakin Skywalker"},
    {"question": "Anakin Skywalker grew up to be who?",
        "answer": "Darth Vader"},
    {"question": "What species is Chewbacca?",
        "answer": "Wookiee"}]


def main(data):
    user_correct_answers=0
    user_wrong_answers=0
    wrong_answers=[]
    
    for q_data in data:
        question=q_data['question']
        correct_answer=q_data['answer']
        user_answer=str(input(f'{question}'))
        if user_answer.strip().lower() == correct_answer.lower():
            user_correct_answers +=1
            print(f'You are right')
        else:
            user_wrong_answers+=1
            print(f'Huh, no, correct answer:{correct_answer}')
            wrong_answers.append((question,user_answer,correct_answer))
    return user_correct_answers,user_wrong_answers,wrong_answers

def print_results(user_correct_answers,user_wrong_answers,wrong_answers):
    print(f"\nQuiz Completed!\nCorrect: {user_correct_answers} | Incorrect: {user_wrong_answers}")
    if user_wrong_answers>0:
        print("\nYour wrong answers:")
        for question, user_answer, correct_answer in wrong_answers:
                print(f"Q: {question}\nYour answer: {user_answer}\nCorrect answer: {correct_answer}\n{'-'*30}")
    
def again():
    data = [
        {"question": "What is Baby Yoda's real name?", "answer": "Grogu"},
        {"question": "Where did Obi-Wan take Luke after his birth?", "answer": "Tatooine"},
        {"question": "What year did the first Star Wars movie come out?", "answer": "1977"},
        {"question": "Who built C-3PO?", "answer": "Anakin Skywalker"},
        {"question": "Anakin Skywalker grew up to be who?", "answer": "Darth Vader"},
        {"question": "What species is Chewbacca?", "answer": "Wookiee"}
    ]
    
    user_correct_answers,user_wrong_answers,wrong_answers = main(data)
    print_results(user_correct_answers,user_wrong_answers,wrong_answers)

    if user_wrong_answers > 3:
        if input("More than 3 wrong answers. Try again? (yes/no): ").strip().lower() == 'yes':
            print("Restart")
            main(data)
        else:
            print("Thanks!")
again()

# user_answer=(input(f'Your answer:'))
# if user_answer == correct_answer:
#     print('You are right')
# else:
        

# for b in range(0,end,1):
#     correct_answer=(data[b].get('answer'))

# main()

# def quiz(*question):
# for i in range(0,end,1):
#     qustion=(data[i].get('question'))
#     main()
    

        # answer=(data[0:i])
        # answer.get('answer')
        # print(f'The answer is {answer}')
        # i+=1
        # continue

# quiz()