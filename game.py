# game.py

# Dependencies
import pygame
import random

def draw_board(screen, board, background):
    # Draw the background image
    screen.blit(background, (0, 0))

    # Draw the grid lines
    # Vertical Lines
    pygame.draw.line(screen, (255, 255, 255), (200, 0), (200, 600), 5)
    pygame.draw.line(screen, (255, 255, 255), (400, 0), (400, 600), 5)
    # Horizontal Lines
    pygame.draw.line(screen, (255, 255, 255), (0, 200), (600, 200), 5)
    pygame.draw.line(screen, (255, 255, 255), (0, 400), (600, 400), 5)

    # Draw the X and O characters
    for row in range(3):
        for col in range(3):
            if board[row][col] == 'X':
                pygame.draw.line(screen, (255, 255, 255), (col * 200 + 50, row * 200 + 50), (col * 200 + 150, row * 200 + 150), 5)
                pygame.draw.line(screen, (255, 255, 255), (col * 200 + 50, row * 200 + 150), (col * 200 + 150, row * 200 + 50), 5)
            elif board[row][col] == 'O':
                pygame.draw.circle(screen, (255, 255, 255), (col * 200 + 100, row * 200 + 100), 50, 5)

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

def cpu_move(board):
    empty_cells = [(r,c) for r in range(3) for c in range(3) if board[r][c] == '']
    if empty_cells:
        row, col = random.choice(empty_cells)
        board[row][col] = 'O'

def display_message(screen, message):
    font = pygame.font.Font('assets/fonts/PressStart2P-Regular.ttf', 40)
    text = font.render(message, True, (255, 255, 255))
    text_rect = text.get_rect(center=(screen.get_width() // 2, screen.get_height() // 2)) 
    screen.blit(text, text_rect)
    pygame.display.flip()

    pygame.time.wait(3000)

def one_player_game(screen):
    print("Starting one player game")

    # Load background image
    background = pygame.image.load('assets/images/ttt_background.png')
    background = pygame.transform.scale(background, (screen.get_width(), screen.get_height()))

    # Initialize the game board
    board = [['' for _ in range(3)] for _ in range(3)]
    game_over = False
    winner = None

    # Draw the initial game state
    draw_board(screen,board,background)
    pygame.display.update()

    while not game_over:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1: # Left mouse button
                    mouse_pos = pygame.mouse.get_pos()
                    row = mouse_pos[1] // 200
                    col = mouse_pos[0] // 200
                    if board[row][col] == '':
                        board[row][col] = 'X'
                        winner = check_winner(board)
                        if winner or all(cell != '' for row in board for cell in row):
                            game_over = True
                        else:
                            cpu_move(board)
                            winner = check_winner(board)
                            if winner:
                                game_over = True

        draw_board(screen,board,background)
        pygame.display.update()

    # Handle game over
    if winner:
        message = f"Game Over! Winner: {winner}"
    else:
        message = "Game Over! It's a draw!"

    display_message(screen, message)
    pygame.display.update()

pygame.quit()