import pygame

def show_options(screen):
    font = pygame.font.Font('assets/fonts/PressStart2P-Regular.ttf', 36)
    music_button = pygame.Rect(150, 200, 300, 50)
    sound_button = pygame.Rect(150, 300, 300, 50)
    difficulty_button = pygame.Rect(150, 400, 300, 50)

    # draw buttons
    pygame.draw.rect(screen, (0, 128, 255), music_button)
    pygame.draw.rect(screen, (0, 128, 255), sound_button)
    pygame.draw.rect(screen, (0, 128, 255), difficulty_button)

    # add text to buttons
    screen.blit(font.render('Music On/Off', True, (255, 255, 255)), (music_button.x + 60, music_button.y + 10))
    screen.blit(font.render('Sound On/Off', True, (255, 255, 255)), (sound_button.x + 60, sound_button.y + 10))
    screen.blit(font.render('Difficulty: Easy/Hard', True, (255, 255, 255)), (difficulty_button.x + 60, difficulty_button.y + 10))

    pygame.display.flip()
