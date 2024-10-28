# menu.py

# Dependencies
import pygame
from utils import render_centered_text

# Color Constants
WHITE = (255, 255, 255)
BLUE = (0, 128, 255)
LIGHT_BLUE = (173, 216, 230)

def show_menu(screen):
    # Load background image
    background = pygame.image.load('assets/images/background.png')
    background = pygame.transform.scale(background, (screen.get_width(), screen.get_height()))

    # Load a font and render the title
    title_font = pygame.font.Font('assets/fonts/PressStart2P-Regular.ttf', 54)
    button_font = pygame.font.Font('assets/fonts/PressStart2P-Regular.ttf', 24)
    
    # Render the title
    title_text = title_font.render('Tic Tac Toe', True, WHITE)

    # Create buttons
    buttons = {
        'one_player': pygame.Rect(175, 250, 450, 60),
        'two_player': pygame.Rect(175, 350, 450, 60),
        'options': pygame.Rect(175, 450, 450, 60)
    }
    
    while True:
        # Get mouse position
        mouse_pos = pygame.mouse.get_pos()

        # Draw menu
        screen.blit(background, (0, 0))
        screen.blit(title_text, (screen.get_width() // 2 - title_text.get_width() // 2, 100))

        # Draw buttons and check for hover
        for label, button in buttons.items():
            color = LIGHT_BLUE if button.collidepoint(mouse_pos) else BLUE
            pygame.draw.rect(screen, color, button)
            render_centered_text(screen, label.replace('_', ' ').title(), button_font, WHITE, button)

        # Check for events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return 'quit'
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                for label, button in buttons.items():
                    if button.collidepoint(mouse_pos):
                        return label

        pygame.display.update()

def choose_symbol(screen):
    # Load background image
    background = pygame.image.load('assets/images/background.png')
    background = pygame.transform.scale(background, (screen.get_width(), screen.get_height()))
    
    button_font = pygame.font.Font('assets/fonts/PressStart2P-Regular.ttf', 40)

    title_text = button_font.render('Choose Your Symbol', True, WHITE)

    x_button = pygame.Rect(275, 250, 100, 100)
    o_button = pygame.Rect(425, 250, 100, 100)

    while True:
        mouse_pos = pygame.mouse.get_pos()

        x_color = LIGHT_BLUE if x_button.collidepoint(mouse_pos) else BLUE
        o_color = LIGHT_BLUE if o_button.collidepoint(mouse_pos) else BLUE

        screen.blit(background, (0, 0))
        screen.blit(title_text, (screen.get_width() // 2 - title_text.get_width() // 2, 100))

        pygame.draw.rect(screen, x_color, x_button)
        pygame.draw.rect(screen, o_color, o_button)
        render_centered_text(screen, 'X', button_font, WHITE, x_button)
        render_centered_text(screen, 'O', button_font, WHITE, o_button)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return None
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                if x_button.collidepoint(mouse_pos):
                    return 'X'  # Return the chosen symbol
                elif o_button.collidepoint(mouse_pos):
                    return 'O'  # Return the chosen symbol

        pygame.display.update()