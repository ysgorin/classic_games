# main.py
import pygame
import random
from menu import show_menu, choose_symbol
from game import one_player_game, display_message

# Initialize pygame and mixer
pygame.init()
pygame.mixer.init()

# Set up display
SCREEN_WIDTH, SCREEN_HEIGHT = 800, 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Tic Tac Toe')

def main(): # Main game loop
    run = True
    
    while run:
        # Show the menu screen
        menu_result = show_menu(screen)

        if menu_result == 'quit':
            run = False
        elif menu_result == 'one_player':
            player_symbol = choose_symbol(screen)

            if player_symbol in ['X', 'O']:
                # Randomly choose who goes first
                first_turn = random.choice(['player', 'computer'])
                
                # Display message indicating turn
                message = "You're first!" if first_turn == 'player' else "Computer's first!"
                display_message(screen, message)
                
                # Start the game
                game = one_player_game(screen, player_symbol, first_turn)
                if game is None: # Handle quit from game screen
                    run = False
            else: # Handle quit from symbol selection
                run = False

        pygame.display.update() # Update the display

    pygame.quit() # Quit pygame

if __name__ == '__main__':
    main()