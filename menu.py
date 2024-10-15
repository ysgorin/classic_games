# menu.py

# Dependencies
import pygame

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
    title_text = title_font.render('Tic Tac Toe', True, (255, 255, 255))

    # Create buttons
    one_player_button = pygame.Rect(175, 250, 450, 60)
    two_player_button = pygame.Rect(175, 350, 450, 60)
    options_button = pygame.Rect(175, 450, 450, 60)

    # Set button colors
    button_color = (0, 128, 255) # blue
    hover_color = (173, 216, 230) # light blue
    
    while True:
        # Get mouse position
        mouse_pos = pygame.mouse.get_pos()

        # Check if mouse is hovering over a button
        one_player_color = hover_color if one_player_button.collidepoint(mouse_pos) else button_color
        two_player_color = hover_color if two_player_button.collidepoint(mouse_pos) else button_color
        options_color = hover_color if options_button.collidepoint(mouse_pos) else button_color

        # Draw menu
        screen.blit(background, (0, 0))
        screen.blit(title_text, (screen.get_width() // 2 - title_text.get_width() // 2, 100))

        # Draw buttons
        pygame.draw.rect(screen, one_player_color, one_player_button)
        pygame.draw.rect(screen, two_player_color, two_player_button)
        pygame.draw.rect(screen, options_color, options_button)

        # Add text to buttons
        one_player_text = button_font.render('One Player', True, (255, 255, 255))
        two_player_text = button_font.render('Two Player', True, (255, 255, 255))
        options_text = button_font.render('Options', True, (255, 255, 255))

        # Get text widths and heights to center text
        one_player_text_width, one_player_text_height = one_player_text.get_size()
        two_player_text_width, two_player_text_height = two_player_text.get_size()
        options_text_width, options_text_height = options_text.get_size()

        # Center text in buttons
        screen.blit(one_player_text, (one_player_button.x + (one_player_button.width - one_player_text_width) // 2,
                                    one_player_button.y + (one_player_button.height - one_player_text_height) // 2))
        screen.blit(two_player_text, (two_player_button.x + (two_player_button.width - two_player_text_width) // 2,
                                    two_player_button.y + (two_player_button.height - two_player_text_height) // 2))
        screen.blit(options_text, (options_button.x + (options_button.width - options_text_width) // 2,
                                options_button.y + (options_button.height - options_text_height) // 2))

        # Check for events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return 'quit'
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    if one_player_button.collidepoint(mouse_pos):
                        return 'one_player' # Identifier for one player game
                    elif two_player_button.collidepoint(mouse_pos):
                        return 'two_player' # Identifier for two player game
                    elif options_button.collidepoint(mouse_pos):
                        return 'options' # Identifier for options

        pygame.display.update()

def choose_symbol(screen):
    # Load background image
    background = pygame.image.load('assets/images/background.png')
    background = pygame.transform.scale(background, (screen.get_width(), screen.get_height()))
    
    button_font = pygame.font.Font('assets/fonts/PressStart2P-Regular.ttf', 40)

    title_text = button_font.render('Choose Your Symbol', True, (255, 255, 255))

    x_button = pygame.Rect(275, 250, 100, 100)
    o_button = pygame.Rect(425, 250, 100, 100)

    button_color = (0, 128, 255)  # blue
    hover_color = (173, 216, 230)  # light blue

    while True:
        mouse_pos = pygame.mouse.get_pos()

        x_color = hover_color if x_button.collidepoint(mouse_pos) else button_color
        o_color = hover_color if o_button.collidepoint(mouse_pos) else button_color

        screen.blit(background, (0, 0))
        screen.blit(title_text, (screen.get_width() // 2 - title_text.get_width() // 2, 100))

        pygame.draw.rect(screen, x_color, x_button)
        pygame.draw.rect(screen, o_color, o_button)

        x_text = button_font.render('X', True, (255, 255, 255))
        o_text = button_font.render('O', True, (255, 255, 255))

        screen.blit(x_text, (x_button.x + (x_button.width - x_text.get_width()) // 2,
                             x_button.y + (x_button.height - x_text.get_height()) // 2))
        screen.blit(o_text, (o_button.x + (o_button.width - o_text.get_width()) // 2,
                             o_button.y + (o_button.height - o_text.get_height()) // 2))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return None
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    if x_button.collidepoint(mouse_pos):
                        return 'X'  # Return the chosen symbol
                    elif o_button.collidepoint(mouse_pos):
                        return 'O'  # Return the chosen symbol

        pygame.display.update()