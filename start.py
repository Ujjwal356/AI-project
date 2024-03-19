import pygame
import sys
import tictactoe
import sudoku
import chess

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 600, 400
BG_COLOR = (220, 220, 220)  # Light gray
BUTTON_COLOR = (0, 128, 0)
TEXT_COLOR = (255, 255, 255)
BUTTON_WIDTH, BUTTON_HEIGHT = 200, 50
BUTTON_MARGIN = 20
FPS = 30

# Initialize screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Game Selection")
clock = pygame.time.Clock()

# Font
font = pygame.font.Font(None, 36)

# Function to draw text on screen
def draw_text(text, x, y):
    text_surface = font.render(text, True, TEXT_COLOR)
    text_rect = text_surface.get_rect(center=(x, y))
    screen.blit(text_surface, text_rect)

# Function to create buttons
def create_button(text, x, y):
    pygame.draw.rect(screen, BUTTON_COLOR, (x - BUTTON_WIDTH // 2, y - BUTTON_HEIGHT // 2, BUTTON_WIDTH, BUTTON_HEIGHT))
    draw_text(text, x, y)

# Main loop
selected_game = None
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos()
            if WIDTH // 2 - BUTTON_WIDTH // 2 <= mouse_pos[0] <= WIDTH // 2 + BUTTON_WIDTH // 2:
                if HEIGHT // 2 - BUTTON_HEIGHT <= mouse_pos[1] <= HEIGHT // 2 - BUTTON_HEIGHT // 2 + BUTTON_HEIGHT:
                    selected_game = "Tic Tac Toe"
                elif HEIGHT // 2 + BUTTON_MARGIN <= mouse_pos[1] <= HEIGHT // 2 + BUTTON_MARGIN + BUTTON_HEIGHT:
                    selected_game = "Sudoku"
                elif HEIGHT // 2 + 2 * BUTTON_MARGIN + BUTTON_HEIGHT <= mouse_pos[1] <= HEIGHT // 2 + 2 * BUTTON_MARGIN + 2 * BUTTON_HEIGHT:
                    selected_game = "Chess"
                    
    if selected_game:
        if selected_game == "Tic Tac Toe":
            tictactoe.__main__()
        elif selected_game == "Sudoku":
            sudoku.__main__()
        elif selected_game == "Chess":
            chess.__main__()
        selected_game = None  # Reset selected game after launching

    screen.fill(BG_COLOR)
    create_button("Tic Tac Toe", WIDTH // 2, HEIGHT // 2 - BUTTON_MARGIN)
    create_button("Sudoku", WIDTH // 2, HEIGHT // 2 + BUTTON_MARGIN)
    create_button("Chess", WIDTH // 2, HEIGHT // 2 + 2 * BUTTON_MARGIN + BUTTON_HEIGHT)
    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()
sys.exit()
