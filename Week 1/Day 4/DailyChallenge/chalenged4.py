    # 7ii
    # Tsx
    # h%?
    # i #
    # sM 
    # $a 
    # #t%
    # ^r!

matrix=[
    ['7','i','i'],
    ['T','s','x'],
    ['h','%','?'],
    ['i',' ','#'],
    ['s','M',' '],
    ['$','a',' '],
    ['#','t','%'],
    ['^','r','!']
]

letters=''

columns=len(matrix[0])
for col in range(columns):
    message=''
    for row in range(len(matrix)):
        char=matrix[row][col]
        if char.isalpha():
            message+=char
    if message:
        letters+=message

letters=letters.strip()
print(letters)