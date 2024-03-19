from flask import Flask, render_template, jsonify, request

app = Flask(__name__)

# Global variable to store the game state
game_state = {
    'board': [
        ['r', 'n', 'b', 'q', 'k', 'b', 'n', 'r'],
        ['p', 'p', 'p', 'p', 'p', 'p', 'p', 'p'],
        [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
        [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
        [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
        [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
        ['P', 'P', 'P', 'P', 'P', 'P', 'P', 'P'],
        ['R', 'N', 'B', 'Q', 'K', 'B', 'N', 'R']
    ],
    'status': 'Waiting for player move...',
    'current_player': 'white'  # Keeps track of whose turn it is
}

def is_valid_move(move):
    # Extract move details
    row, col = move['row'], move['col']
    new_row, new_col = move['new_row'], move['new_col']
    piece = game_state['board'][row][col]
    new_square = game_state['board'][new_row][new_col]

    # Check if it's the player's piece
    if (piece.isupper() and game_state['current_player'] != 'white') or (piece.islower() and game_state['current_player'] != 'black'):
        return False

    # Define movement rules for each piece type
    if piece.lower() == 'p':
        if piece.islower():  # Black pawn
            if row == 6:  # First move for black pawns
                return new_row in {row - 1, row - 2} and new_col == col and new_square == ' '
            else:
                return new_row == row - 1 and new_col == col and new_square == ' '
        else:  # White pawn
            if row == 1:  # First move for white pawns
                return new_row in {row + 1, row + 2} and new_col == col and new_square == ' '
            else:
                return new_row == row + 1 and new_col == col and new_square == ' '
    elif piece.lower() == 'r':
        return (new_row == row or new_col == col) and is_clear_path(row, col, new_row, new_col)
    elif piece.lower() == 'n':
        return (abs(new_row - row) == 2 and abs(new_col - col) == 1) or (abs(new_row - row) == 1 and abs(new_col - col) == 2)
    elif piece.lower() == 'b':
        return abs(new_row - row) == abs(new_col - col) and is_clear_diagonal(row, col, new_row, new_col)
    elif piece.lower() == 'q':
        return (new_row == row or new_col == col or abs(new_row - row) == abs(new_col - col)) and (is_clear_path(row, col, new_row, new_col) or is_clear_diagonal(row, col, new_row, new_col))
    elif piece.lower() == 'k':
        return abs(new_row - row) <= 1 and abs(new_col - col) <= 1

def is_clear_path(row, col, new_row, new_col):
    step_row = 0 if row == new_row else (new_row - row) // abs(new_row - row)
    step_col = 0 if col == new_col else (new_col - col) // abs(new_col - col)
    r, c = row + step_row, col + step_col
    while (r, c) != (new_row, new_col):
        if game_state['board'][r][c] != ' ':
            return False
        r, c = r + step_row, c + step_col
    return True

def is_clear_diagonal(row, col, new_row, new_col):
    step_row = (new_row - row) // abs(new_row - row)
    step_col = (new_col - col) // abs(new_col - col)
    r, c = row + step_row, col + step_col
    while (r, c) != (new_row, new_col):
        if game_state['board'][r][c] != ' ':
            return False
        r, c = r + step_row, c + step_col
    return True

def apply_move(move):
    global game_state
    if is_valid_move(move):
        row, col = move['row'], move['col']
        piece = game_state['board'][row][col]
        game_state['board'][row][col] = ' '  # Clear the current square
        new_row, new_col = move['new_row'], move['new_col']
        game_state['board'][new_row][new_col] = piece  # Move the piece to the new square
        game_state['status'] = 'Move successful'
        game_state['current_player'] = 'black' if game_state['current_player'] == 'white' else 'white'
    else:
        game_state['status'] = 'Invalid move'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/move', methods=['POST'])
def move():
    global game_state
    move = request.json
    apply_move(move)
    return jsonify(game_state)

if __name__ == '__main__':
    app.run(debug=True)
