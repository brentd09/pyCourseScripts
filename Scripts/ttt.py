def show_board(game_board):
    os.system('cls')
    for row in range(0,7,3):
        print('',game_board[0+row],'|',game_board[1+row],'|',game_board[2+row])
        print('---+---+---' if row < 5 else '')

def check_for_win(game_board):
    # print(game_board)
    for row in range(3):
        if game_board[0+row] == game_board[3+row] == game_board[6+row]:
          return True
    for col in range(0,7,3):
        if game_board[0+col] == game_board[1+col] == game_board[2+col]:
          return True
    for d1, d2, d3 in [[0,4,8],[2,4,6]]:
        if game_board[d1] == game_board[d2] == game_board[d3]:
            return True        
    return False      


import os
this_move = 'X'
board = ['1','2','3','4','5','6','7','8','9']
setboard = set(board.copy())
won = False
while set(board).intersection(setboard):
    show_board(board)
    prmpt = 'Pick a number for your move for ' + this_move + ': '
    choice = '0'
    while choice not in board:
      choice = input(prmpt)
    board[int(choice)-1 ] = this_move
    won = check_for_win(board)
    if not won:
        this_move = 'O' if this_move == 'X' else 'X'
    else:
        break
show_board(board)
game_result = ('The winner is: ' + this_move) if won else 'The game is a draw'
print(game_result)

