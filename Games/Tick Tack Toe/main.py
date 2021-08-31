board_ttt = {
    1: ' ',
    2: ' ',
    3: ' ',
    4: ' ',
    5: ' ',
    6: ' ',
    7: ' ',
    8: ' ',
    9: ' ',
}

def print_board(board):
    print(f'| {board[1]} | {board[2]} | {board[3]} |')
    print('----+---+----')
    print(f'| {board[4]} | {board[5]} | {board[6]} |')
    print('----+---+----')
    print(f'| {board[7]} | {board[8]} | {board[9]} |')
    print('----+---+----')

def main():
    player = ['Player 1', 'Player 2']

    player1_mark = 'X'
    player2_mark = 'O'

    for i in range(10):
        print_board(board_ttt)
        current_player = player[i % 2]


        if board_ttt[5] == board_ttt[1] == board_ttt[9] == 'X':
            print('Player 1 win!')
            break
        
        if board_ttt[2] == board_ttt[5] == board_ttt[8] == 'X':
            print('Player 1 win!')
            break

        if board_ttt[3] == board_ttt[5] == board_ttt[7] == 'X':
            print('Player 1 win')
            break

        if board_ttt[4] == board_ttt[5] == board_ttt[6] == 'X':
            print('Player 1 win')
            break

        if board_ttt[1] == board_ttt[2] == board_ttt[3] == 'X':
            print('Player 1 win')
            break

        if board_ttt[7] == board_ttt[8] == board_ttt[9] == 'X':
            print('Player 1 win')
            break

        if board_ttt[5] == board_ttt[1] == board_ttt[9] == 'O':
            print('Player 2 win!')
            break
       
        if board_ttt[2] == board_ttt[5] == board_ttt[8] == 'O':
            print('Player 2 win!')
            break

        if board_ttt[3] == board_ttt[5] == board_ttt[7] == 'O':
            print('Player 2 win')
            break

        if board_ttt[4] == board_ttt[5] == board_ttt[6] == 'O':
            print('Player 2 win')
            break

        if board_ttt[1] == board_ttt[2] == board_ttt[3] == 'O':
            print('Player 2 win')
            break

        if board_ttt[7] == board_ttt[8] == board_ttt[9] == 'O':
            print('Player 2 win')
            break

        if current_player == 'Player 1':
            print('Player 1: it\'s your turn:')
            move = int(input())

            if board_ttt[move] == ' ':
                board_ttt[move] = player1_mark
            else:
                print('invalid input')
                continue

        elif current_player == 'Player 2':
            print('Player 2: it\'s your turn:')
            move  = int(input())
            
            if board_ttt[move] == ' ':
                board_ttt[move] = player2_mark
            else:
                print('invalid input')
                continue


if __name__ == '__main__':
    main()
