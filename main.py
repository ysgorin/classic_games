# main.py
import pygame
from menu import show_menu, choose_symbol
from game import one_player_game

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
                game = one_player_game(screen, player_symbol)
                if game == None:
                    run = False
            elif player_symbol == None:
                run = False

        # Update the display
        pygame.display.update()

    pygame.quit()

if __name__ == '__main__':
    main()