# main.py
import pygame
from menu import show_menu
from game import one_player_game

# Initialize pygame
pygame.init()

# Set up display
screen = pygame.display.set_mode((800,600))
pygame.display.set_caption('Tic Tac Toe')

# Main game loop
def main():
    run = True
    while run:
        # Show the menu screen
        menu_result = show_menu(screen)
        if menu_result == 'quit':
            run = False
        if menu_result == 'one_player':
            one_player_game(screen)

        # Update the display
        pygame.display.update()

    pygame.quit()

if __name__ == '__main__':
    main()