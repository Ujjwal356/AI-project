import pygame
import sys
import random

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 600, 600
BG_COLOR = (255, 255, 255)
LINE_COLOR = (0, 0, 0)
LINE_WIDTH = 10
BOARD_ROWS, BOARD_COLS = 3, 3
SQUARE_SIZE = WIDTH // BOARD_COLS
CROSS_COLOR = (255, 0, 0)
CIRCLE_COLOR = (0, 0, 255)

# Screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Tic Tac Toe")
screen.fill(BG_COLOR)

# Board
board = [['' for _ in range(BOARD_COLS)] for _ in range(BOARD_ROWS)]


def draw_lines():
    # Horizontal lines
    pygame.draw.line(screen, LINE_COLOR, (0, SQUARE_SIZE), (WIDTH, SQUARE_SIZE), LINE_WIDTH)
    pygame.draw.line(screen, LINE_COLOR, (0, 2 * SQUARE_SIZE), (WIDTH, 2 * SQUARE_SIZE), LINE_WIDTH)
    # Vertical lines
    pygame.draw.line(screen, LINE_COLOR, (SQUARE_SIZE, 0), (SQUARE_SIZE, HEIGHT), LINE_WIDTH)
    pygame.draw.line(screen, LINE_COLOR, (2 * SQUARE_SIZE, 0), (2 * SQUARE_SIZE, HEIGHT), LINE_WIDTH)


def draw_figures():
    for row in range(BOARD_ROWS):
        for col in range(BOARD_COLS):
            if board[row][col] == 'O':
                pygame.draw.circle(screen, CIRCLE_COLOR, (int(col * SQUARE_SIZE + SQUARE_SIZE / 2),
                                                           int(row * SQUARE_SIZE + SQUARE_SIZE / 2)), SQUARE_SIZE // 3,
                                   LINE_WIDTH)
            elif board[row][col] == 'X':
                pygame.draw.line(screen, CROSS_COLOR,
                                 (col * SQUARE_SIZE + LINE_WIDTH, row * SQUARE_SIZE + LINE_WIDTH),
                                 ((col + 1) * SQUARE_SIZE - LINE_WIDTH, (row + 1) * SQUARE_SIZE - LINE_WIDTH), LINE_WIDTH)
                pygame.draw.line(screen, CROSS_COLOR,
                                 ((col + 1) * SQUARE_SIZE - LINE_WIDTH, row * SQUARE_SIZE + LINE_WIDTH),
                                 (col * SQUARE_SIZE + LINE_WIDTH, (row + 1) * SQUARE_SIZE - LINE_WIDTH), LINE_WIDTH)


def mark_square(row, col, player):
    board[row][col] = player


def is_square_empty(row, col):
    return board[row][col] == ''


def check_win(player):
    # Check rows
    for row in range(BOARD_ROWS):
        if board[row][0] == player and board[row][1] == player and board[row][2] == player:
            return True
    # Check columns
    for col in range(BOARD_COLS):
        if board[0][col] == player and board[1][col] == player and board[2][col] == player:
            return True
    # Check diagonals
    if board[0][0] == player and board[1][1] == player and board[2][2] == player:
        return True
    if board[0][2] == player and board[1][1] == player and board[2][0] == player:
        return True
    return False


def is_board_full():
    for row in range(BOARD_ROWS):
        for col in range(BOARD_COLS):
            if board[row][col] == '':
                return False
    return True


def get_available_moves():
    moves = []
    for row in range(BOARD_ROWS):
        for col in range(BOARD_COLS):
            if board[row][col] == '':
                moves.append((row, col))
    return moves


def minimax(board, depth, is_maximizing):
    if check_win('X'):
        return -10 + depth
    elif check_win('O'):
        return 10 - depth
    elif is_board_full():
        return 0

    if is_maximizing:
        best_score = -float('inf')
        for move in get_available_moves():
            row, col = move
            board[row][col] = 'O'
            score = minimax(board, depth + 1, False)
            board[row][col] = ''
            best_score = max(score, best_score)
        return best_score
    else:
        best_score = float('inf')
        for move in get_available_moves():
            row, col = move
            board[row][col] = 'X'
            score = minimax(board, depth + 1, True)
            board[row][col] = ''
            best_score = min(score, best_score)
        return best_score


def get_best_move():
    best_score = -float('inf')
    best_move = None
    for move in get_available_moves():
        row, col = move
        board[row][col] = 'O'
        score = minimax(board, 0, False)
        board[row][col] = ''
        if score > best_score:
            best_score = score
            best_move = move
    return best_move


def restart_game():
    screen.fill(BG_COLOR)
    draw_lines()
    for row in range(BOARD_ROWS):
        for col in range(BOARD_COLS):
            board[row][col] = ''
    pygame.display.flip()


# Game loop
player_turn = 'X'
game_over = False
mode = input("Choose mode: 'pvp' for Player vs Player or 'pvc' for Player vs Computer: ").lower()
while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN and not game_over:
            mouseX = event.pos[0]
            mouseY = event.pos[1]
            clicked_row = mouseY // SQUARE_SIZE
            clicked_col = mouseX // SQUARE_SIZE
            if is_square_empty(clicked_row, clicked_col):
                mark_square(clicked_row, clicked_col, player_turn)
                if check_win(player_turn):
                    print(f"Player {player_turn} wins!")
                    game_over = True
                elif is_board_full():
                    print("It's a draw!")
                    game_over = True
                else:
                    player_turn = 'O' if player_turn == 'X' else 'X'
                    if mode == 'pvc' and player_turn == 'O':
                        # Computer's turn
                        row, col = get_best_move()
                        mark_square(row, col, player_turn)
                        if check_win(player_turn):
                            print(f"Player {player_turn} wins!")
                            game_over = True
                        elif is_board_full():
                            print("It's a draw!")
                            game_over = True
                        else:
                            player_turn = 'X'
    screen.fill(BG_COLOR)
    draw_lines()
    draw_figures()
    pygame.display.flip()
