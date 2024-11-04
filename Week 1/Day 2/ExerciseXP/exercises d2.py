# # Exercise 1 Favorite Numbers
# # Create a set called my_fav_numbers with all your favorites numbers.
# my_fav_numbers={1,2,13,26,33,36}
# # Add two new numbers to the set.
# my_fav_numbers.add(3)
# my_fav_numbers.add(11)
# # Remove the last number.
# my_fav_numbers.pop()
# print(my_fav_numbers)
# # Create a set called friend_fav_numbers with your friend’s favorites numbers.
# friend_fav_numbers={2,23,9,11,13}
# # Concatenate my_fav_numbers and friend_fav_numbers to a new variable called our_fav_numbers.
# our_fav_numbers=my_fav_numbers.union(friend_fav_numbers)
# print(our_fav_numbers)

# # Exercise 2 Tuple
# # Given a tuple which value is integers, is it possible to add more integers to the tuple?
# # No = tuples are immutable


# # Exercise 3 List
# basket=["Banana","Apples","Oranges","Blueberries"]
# # Remove “Banana” from the list.
# basket.remove("Banana")
# # Remove “Blueberries” from the list.
# basket.remove("Blueberries")
# # Add “Kiwi” to the end of the list.
# basket.append("Kiwi")
# # Add “Apples” to the beginning of the list.
# basket.append("Apples")
# print(basket)
# # Count how many apples are in the basket.
# print(basket.count("Apples"))
# # Empty the basket.
# del basket[0:]   # basket.clear()
# # Print(basket)
# print(basket)

# # Exercise 4 Floats
# # Create a list containing the following sequence 1.5, 2, 2.5, 3, 3.5, 4, 4.5, 5 (don’t hard-code the sequence).
# new_list=[1.5,2,2.5,3,3.5,4,4.5,5]
# print(new_list)
# new_list.append(5.5)
# print(new_list)

# # Exercise 5 For loop
# # Use a for loop to print all numbers from 1 to 20, inclusive.
# for num in range(1,21):
#     print(num)
# # Using a for loop, that loops from 1 to 20(inclusive), print out every element which has an even index.
# for num in range(1,21,2):
#         print(num)

# # Exercise 6 While Loop
# # Write a while loop that will continuously ask the user for their name, unless the input is equal to your name.
# user_name=input('What is your name?')
# keep_asking=True
# while keep_asking:
#     if user_name == 'Kirill':
#         keep_asking=False
#     else:
#         user_name = input('What is your name?')


# # Exercise 7 Favorite Fruits
# # Ask the user to input their favorite fruit(s) (one or several fruits).
# fav_fruits=input("Whats your favorite fruits?Separate them with a single space!")
# #Store the favorite fruit(s) in a list (convert the string of words into a list of words).
# fav_fruits=list(fav_fruits.split(" "))
# print(fav_fruits)
# # Now that we have a list of fruits, ask the user to input a name of any fruit.
# # If the user’s input is in the favorite fruits list, print “You chose one of your favorite fruits! Enjoy!”.
# # If the user’s input is NOT in the list, print, “You chose a new fruit. I hope you enjoy”.
# fav_fruits=set(fav_fruits)
# any_fruit=input(('Name any fruit:'))
# any_fruit=list(any_fruit.split(" "))
# any_fruit=set(any_fruit)
# if any_fruit<=fav_fruits:
#      print("You chose one of your favorite fruits!Enjoy!")
# else:
#      print("You chose a new fruit.I hope you enjoy")
     

#Exercise Who ordered a pizza?
#Write a loop that asks a user to enter a series of pizza toppings, when the user inputs ‘quit’ stop asking for toppings.
# pizza= []
# keep_asking=True
# while keep_asking:
#     toppings = input('Which toppings you want? press "quit" to stop:')
#     if toppings != 'quit':
#         pizza.append(toppings)
#         print(f'You will add {toppings} to your pizza')
#     if toppings == 'quit':
#         keep_asking=False

# topping_price=len(pizza)*2.5
# price=10+topping_price
# print(f'Your pizza with {pizza}, and its total price is {price}')

#As they enter each topping, print a message saying you’ll add that topping to their pizza.
#Upon exiting the loop print all the toppings on the pizza pie and what the total price is (10 + 2.5 for each topping).


# Exercise 9 Cinemax
#     A movie theater charges different ticket prices depending on a person’s age
# user_age=input('Enter age of a family member or press "q":')
family=0
while True:
    user_age=input('Enter age of a family member or press "q":')

    if user_age== "q":
        break
    try:
        age=int(user_age)

        if age<3:
            ticket=0
        elif 3<=age<=12:
            ticket=10
        else:
            ticket=15
    
        family += ticket
    except ValueError:
        print('!')

print(f"The total cost of all tickets is: ${family}")
#Ask a family the age of each person who wants a ticket.
#Store the total cost of all the family’s tickets and print it out.
#A group of teenagers are coming to your movie theater and want to watch a movie that is restricted for people between the ages of 16 and 21.
# Given a list of names, write a program that asks teenager for their age, if they are not permitted to watch the movie, remove them from the list.
# At the end, print the final list.


# Exercise 10 Sandwich Orders
sandwich_orders = ["Tuna sandwich", "Pastrami sandwich", "Avocado sandwich", "Pastrami sandwich", "Egg sandwich", "Chicken sandwich", "Pastrami sandwich"]
