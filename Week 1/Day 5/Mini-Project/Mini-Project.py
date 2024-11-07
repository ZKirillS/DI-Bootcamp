list_board=[
    [' ',' ',' '],
    [' ',' ',' '],
    [' ',' ',' '],
]


def display(list_board):
    print('TIC TAC TOE')
    print('*'*9)
    for board in list_board:
        print('*--|-|--*')
        print(' '.join(board))
    print('*--|-|--*')
    print('*'*9)

display(list_board)


def player_input1(user):
    print(f'Players {user} turn...')
    user1_row=int(input('Enter row(0,1,2):'))
    user1_column=int(input('Enter column(0,1,2):'))
    letter=list_board[user1_row][user1_column]
    while letter!=' ':
        user1_column=int(input(f'player {user} Choose column(0,1,2):'))
        user1_row=int(input(f'player {user} Choose the row(0,1,2):'))

    list_board[user1_row][user1_column] = user
    display(list_board)
    

def check_win():

    win_combination = [
        [(0,0), (0,1), (0,2)],
        [(1,0), (1,1), (1,2)],
        [(2,0), (2,1), (2,2)],
        [(0,0), (1,0), (2,0)],
        [(0,1), (1,1), (2,1)],
        [(0,2), (1,2), (2,2)],
        [(0,0), (1,1), (2,2)],
        [(0,2), (1,1), (2,0)]
        ]
    player_simbols = ['X', 'O']
    for simbols in player_simbols:
        for lists in win_combination:
            player_count = 0
            for position in lists:
                if list_board[position[0]][position[-1]] == simbols:
                    player_count += 1    
                    if player_count==3:
                        print(f'{simbols} wins!')
                        return True                   
        else:
            break


def check_draw():
    for row in list_board:
        if ' ' in row:
            return False  
    return True
      
def play():
    turn_count=0
    while True:
        player_input1('X')
        turn_count+=1
        if check_win()==True:
            print('Player X win!')
            break
        elif check_draw() or turn_count==9:
            print('Its a draw!')
            break
        player_input1('O')
        turn_count+=1
        if check_win()==True:
            print('Player O win!')
            break
        elif check_draw() or turn_count==9:
            print('Its a draw!')
            break

play()