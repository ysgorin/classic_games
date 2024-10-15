# menu.py

# Dependencies
import pygame

def show_menu(screen):
    # Load background image
    background = pygame.image.load('assets/images/ttt_background.png')
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