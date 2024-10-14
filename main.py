import pygame
from menu import show_menu

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
        show_menu(screen)

        # Event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        # Update the display
        pygame.display.update()

    pygame.quit()

if __name__ == '__main__':
    main()