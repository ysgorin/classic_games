# game.py

# Dependencies
import pygame
import random
import time
from utils import render_centered_text

pygame.init()

# Constants for screen size, grid, and colors
SCREEN_WIDTH, SCREEN_HEIGHT = 800, 600
GRID_SIZE = 600  # Size of the grid area (square)
CELL_SIZE = GRID_SIZE // 3  # Size of each cell (200x200)
WHITE = (255, 255, 255)
BLUE = (0, 128, 255)

# Sound Effect
SOUND_EFFECT = pygame.mixer.Sound('assets/audio/MA_SoundCreator_Pen_Clicks_1.wav')

def draw_board(screen, board, background):
    # Draw the background image
    screen.blit(background, (0, 0))

    # Calculate grid offset to center it on the screen
    x_offset = (SCREEN_WIDTH - GRID_SIZE) // 2
    y_offset = (SCREEN_HEIGHT - GRID_SIZE) // 2

    # Draw grid lines
    for i in range(1, 3):
        pygame.draw.line(screen, WHITE, (x_offset + i * CELL_SIZE, y_offset), 
                         (x_offset + i * CELL_SIZE, y_offset + GRID_SIZE), 5)
        pygame.draw.line(screen, WHITE, (x_offset, y_offset + i * CELL_SIZE), 
                         (x_offset + GRID_SIZE, y_offset + i * CELL_SIZE), 5)

    # Draw symbols
    font = pygame.font.Font('assets/fonts/PressStart2P-Regular.ttf', 80)
    for row in range(3):
        for col in range(3):
            if board[row][col] != '':
                text = font.render(board[row][col], True, WHITE)
                text_rect = text.get_rect(center=(
                    x_offset + col * CELL_SIZE + CELL_SIZE // 2,
                    y_offset + row * CELL_SIZE + CELL_SIZE // 2
                ))
                screen.blit(text, text_rect)

def check_winner(board):
    # Check rows, columns, and diagonals for a winner
    for row in board:
        if row[0] == row[1] == row[2] and row[0] != '':
            return row[0]
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] and board[0][col] != '':
            return board[0][col]
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != '': 
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != '':
        return board[0][2]
    return None

def cpu_move(board, cpu_symbol):
    empty_cells = [(r,c) for r in range(3) for c in range(3) if board[r][c] == '']
    if empty_cells:
        row, col = random.choice(empty_cells)
        board[row][col] = cpu_symbol

def display_message(screen, message):
    # Load background image
    background = pygame.image.load('assets/images/background.png')
    background = pygame.transform.scale(background, (screen.get_width(), screen.get_height()))
    screen.blit(background, (0, 0))

    # Set up the font and render the message
    font = pygame.font.Font('assets/fonts/PressStart2P-Regular.ttf', 40)
    text = font.render(message, True, WHITE)
    text_rect = text.get_rect(center=(screen.get_width() // 2, screen.get_height() // 2)) 
    screen.blit(text, text_rect)

    pygame.display.flip()
    time.sleep(2)

def one_player_game(screen, player_symbol, first_turn):
    cpu_symbol = 'O' if player_symbol == 'X' else 'X'

    # Load background image
    background = pygame.image.load('assets/images/background.png')
    background = pygame.transform.scale(background, (screen.get_width(), screen.get_height()))

    # Initialize the game board
    board = [['' for _ in range(3)] for _ in range(3)]
    game_over = False
    winner = None

    # Draw the initial game state
    draw_board(screen,board,background)
    pygame.display.update()

    # If computer goes first, make the initial move
    if first_turn == 'computer':
        cpu_move(board, cpu_symbol)
        SOUND_EFFECT.play()
        draw_board(screen, board, background)
        pygame.display.update()

    while not game_over:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:  # Left mouse button
                mouse_pos = pygame.mouse.get_pos()
                x_offset = (SCREEN_WIDTH - GRID_SIZE) // 2
                y_offset = (SCREEN_HEIGHT - GRID_SIZE) // 2
                row, col = (mouse_pos[1] - y_offset) // CELL_SIZE, (mouse_pos[0] - x_offset) // CELL_SIZE
                if 0 <= row < 3 and 0 <= col < 3 and board[row][col] == '':
                    board[row][col] = player_symbol
                    SOUND_EFFECT.play()
                    draw_board(screen,board,background)
                    pygame.display.update()
                    
                    winner = check_winner(board)
                    if winner or all(cell != '' for row in board for cell in row):
                        game_over = True
                    else:
                        time.sleep(1)
                        cpu_move(board, cpu_symbol)
                        SOUND_EFFECT.play()
                        winner = check_winner(board)
                        if winner or all(cell != '' for row in board for cell in row):
                            game_over = True

        draw_board(screen,board,background)
        pygame.display.update()

    # Handle game over
    if winner:
        message = f"Winner: {winner}"
    else:
        message = "Tie Game!"
    time.sleep(1)
    display_message(screen, message)
    pygame.display.update()
    return 'game over'

def two_player_game(screen, player1, player2, first_player):
    background = pygame.image.load('assets/images/background.png')
    background = pygame.transform.scale(background, (screen.get_width(), screen.get_height()))
    board = [['' for _ in range(3)] for _ in range(3)]

    current_player = first_player  # Start with the first player
    current_symbol = 'X' if current_player == player1 else 'O'
    game_over = False
    winner = None

    draw_board(screen, board, background)
    pygame.display.update()

    while not game_over:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return 'quit'
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                mouse_pos = pygame.mouse.get_pos()
                x_offset = (SCREEN_WIDTH - GRID_SIZE) // 2
                y_offset = (SCREEN_HEIGHT - GRID_SIZE) // 2
                row, col = (mouse_pos[1] - y_offset) // CELL_SIZE, (mouse_pos[0] - x_offset) // CELL_SIZE

                if 0 <= row < 3 and 0 <= col < 3 and board[row][col] == '':
                    board[row][col] = current_symbol
                    SOUND_EFFECT.play()
                    draw_board(screen, board, background)
                    pygame.display.update()

                    winner = check_winner(board)
                    if winner or all(cell != '' for row in board for cell in row):
                        game_over = True
                    else:
                        # Switch player and symbol for the next turn
                        current_player = player2 if current_player == player1 else player1
                        current_symbol = 'O' if current_symbol == 'X' else 'X'

    message = f"{current_player} Wins!" if winner else "Tie Game!"
    display_message(screen, message)

    # Ask if players want to play again
    return play_again_prompt(screen)

def play_again_prompt(screen):
    background = pygame.image.load('assets/images/background.png')
    background = pygame.transform.scale(background, (screen.get_width(), screen.get_height()))

    font = pygame.font.Font('assets/fonts/PressStart2P-Regular.ttf', 40)

    yes_button = pygame.Rect(200, 300, 150, 50)
    no_button = pygame.Rect(450, 300, 150, 50)

    while True:
        screen.blit(background, (0, 0))
        render_centered_text(screen, "Play Again?", font, WHITE, pygame.Rect(0, 200, 800, 50))
        pygame.draw.rect(screen, BLUE, yes_button)
        pygame.draw.rect(screen, BLUE, no_button)

        render_centered_text(screen, "Yes", font, WHITE, yes_button)
        render_centered_text(screen, "No", font, WHITE, no_button)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return 'quit'
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                if yes_button.collidepoint(event.pos):
                    return 'play_again'
                elif no_button.collidepoint(event.pos):
                    return 'quit'

        pygame.display.update()