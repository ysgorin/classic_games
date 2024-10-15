# main.py
import pygame
import random
from menu import show_menu, choose_symbol
from game import one_player_game, display_message

# Initialize pygame
pygame.init()

# Initialize the mixer
# pygame.mixer.init()

# Load and play background music
# pygame.mixer.music.load('assets/audio/Atmospheric Ambient Hip Hop.wav')
# pygame.mixer.music.play(-1)  # -1 makes it loop indefinitely

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
            player_symbol = choose_symbol(screen)
            if player_symbol in ['X', 'O']:
                # Randomly choose who goes first
                first_turn = random.choice(['player', 'computer'])
                
                # Show message to indicate turn
                message = "You're first!" if first_turn == 'player' else "Computer's first!"
                display_message(screen, message)

                game = one_player_game(screen, player_symbol, first_turn)
                if game == None:
                    run = False
            elif player_symbol == None:
                run = False

        # Update the display
        pygame.display.update()

    pygame.quit()

if __name__ == '__main__':
    main()