#Challenge 1
# Ask a user for a word
word=input('Print a word:')

# Write a program that creates a dictionary. This dictionary stores the indexes of each letter in a list.
# Make sure the letters are the keys.
# Make sure the letters are strings.
# # Make sure the indexes are stored in a list and those lists are values.
indexes={}
for index,value in enumerate(word):
    if value in indexes:
        indexes[value].append(index)
    else:
        indexes[value]=[index]
print(indexes)

# Create a program that prints a list of the items you can afford in the store with the money you have in your wallet.
# Sort the list in alphabetical order.
# Return “Nothing” if you can’t afford anything from the store.
# Hint : make sure to convert the amount from dollars to numbers. Create a program that deletes the $ sign, and the comma (for thousands)

items_purchase = {
  "Apple": "$14",
  "Cherry": "$5",
  "Chocolate": "$8",
  "Bananas": "$6",
  "Refrigerator": "$1100",
  "Spoon": "$2"
}

wallet= "$150"
walletb=int(wallet.replace('$',''))

cart=0
buys=[]
for key,value in items_purchase.items():
    price=int(value.replace('$','').replace(',',''))
    if cart+price<=walletb:
        buys.append(key)
        cart+=price

if buys:
    print(buys)
else:
    print('Nothing')
