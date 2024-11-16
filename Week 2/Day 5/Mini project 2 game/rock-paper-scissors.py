# Mini Project : Rock Paper Scissors
from game import Game as G

def get_user_menu_choice():
    print('\n   Menu:') # gui
    print('     (g) Play a new game')
    print('     (x) Show scores and exit')

    while True: # menu loop
        u_choose = input('Select option: ')
        if u_choose in ['x','g']:
            return u_choose
        else:
            print('Invalid input. You can choose g or x only.')


def print_results(results):
    print('\n   Game results:')
    print(f'     You won {results['win']} times') # k:v 
    print(f'     You lost {results['loss']} times')
    print(f'     You drew {results['draw']} times')
    print('Thanks for playing!')

def main():
    results = {'win':0,'loss':0,'draw':0} # res dict
    while True:
        menu_choise = get_user_menu_choice()
        if menu_choise == 'g':
            game = G()
            game_result = game.play()

            if game_result == 'win': # possible results
                results['win'] +=1
            if game_result == 'loss':
                results['loss'] +=1
            if game_result == 'draw':
                results['draw'] +=1
        elif menu_choise == 'x':
            print_results(results)
            break
        else:
            print()

if __name__ == "__main__":
    main()