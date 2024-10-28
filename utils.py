# Helper function to render centered text
def render_centered_text(screen, text, font, color, rect):
    rendered_text = font.render(text, True, color)
    text_rect = rendered_text.get_rect(center=rect.center)
    screen.blit(rendered_text, text_rect)