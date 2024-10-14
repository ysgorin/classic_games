# Dependencies
import pygame
import random

def draw_grid(screen):
    # Draw horizontal and vertical lines for the Tic Tac Toe grid
    color = (255, 255, 255)
    pygame.draw.line(screen, color, (200, 100), (200, 400), 5)
    pygame.draw.line(screen, color, (300, 100), (300, 400), 5)
    pygame.draw.line(screen, color, (100, 200), (400, 200), 5)
    pygame.draw.line(screen, color, (100, 300), (400, 300), 5)

    # Add more functions for Xs and Os later

def cpu_move(board):
    
    empty_cells = [i for i, cell in enumerate(board) if cell == '']
    return random.choice(empty_cells)
