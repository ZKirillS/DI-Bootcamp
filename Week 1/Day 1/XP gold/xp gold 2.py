month=int(input('Select a month:'))
if 3<=month<=5:
    print('Spring')
if 6<=month<=8:
    print('Summer')
if 9<=month<=11:
    print('Autumn')
if month==1 or month==2 or month==12:
    print('Winter')
if month==0 or month>12:
    print('Please select a number from 1 to 12')