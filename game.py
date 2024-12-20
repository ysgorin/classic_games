# game.py

# Dependencies
import pygame
import random
import time
from utils import render_centered_text

pygame.init()

# Constants for screen size, grid, and colors
SCREEN_WIDTH, SCREEN_HEIGHT = 800, 600
GRID_SIZE = 390  # Size of the grid area (square)
CELL_SIZE = GRID_SIZE // 3  # Size of each cell (130x130)
WHITE = (255, 255, 255)
BLUE = (0, 128, 255)

# Sound Effect
SOUND_EFFECT = pygame.mixer.Sound('assets/audio/MA_SoundCreator_Pen_Clicks_1.wav')

def draw_board(screen, board, background, turn):
    # Draw the background image
    screen.blit(background, (0, 0))

    # Calculate grid offset to center it on the screen
    x_offset = (SCREEN_WIDTH - GRID_SIZE) * 2 // 3
    y_offset = (SCREEN_HEIGHT - GRID_SIZE) // 2

    # Draw vertical line at 1/3 of the screen width
    pygame.draw.line(screen, WHITE, (SCREEN_WIDTH // 4, 0), (SCREEN_WIDTH // 4, SCREEN_HEIGHT), 5)

    # Draw text indicating whose turn it is
    font = pygame.font.Font('assets/fonts/PressStart2P-Regular.ttf', 16)
    turn_lines = [f"{turn}'s", "turn"] # pygame doesn't support multiline text
    turn_texts = [font.render(line, True, WHITE) for line in turn_lines]
    turn_rects = [text.get_rect(center=(SCREEN_WIDTH // 8, SCREEN_HEIGHT // 4 - 10 + i * 20)) for i, text in enumerate(turn_texts)]
    for text, rect in zip(turn_texts, turn_rects):
        screen.blit(text, rect)

    # Draw grid lines
    for i in range(1, 3):
        pygame.draw.line(screen, WHITE, (x_offset + i * CELL_SIZE, y_offset), 
                         (x_offset + i * CELL_SIZE, y_offset + GRID_SIZE), 5)
        pygame.draw.line(screen, WHITE, (x_offset, y_offset + i * CELL_SIZE), 
                         (x_offset + GRID_SIZE, y_offset + i * CELL_SIZE), 5)

    # Draw symbols
    font = pygame.font.Font('assets/fonts/PressStart2P-Regular.ttf', 50)
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
    turn = 'Player'

    # Load background image
    background = pygame.image.load('assets/images/background.png')
    background = pygame.transform.scale(background, (screen.get_width(), screen.get_height()))

    # Initialize the game board
    board = [['' for _ in range(3)] for _ in range(3)]
    game_over = False
    winner = None

    # Draw the initial game state
    draw_board(screen,board,background,turn)
    pygame.display.update()

    # If computer goes first, make the initial move
    if first_turn == 'computer':
        cpu_move(board, cpu_symbol)
        SOUND_EFFECT.play()
        draw_board(screen,board,background,turn)
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
                    draw_board(screen,board,background,turn)
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

        draw_board(screen,board,background,turn)
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