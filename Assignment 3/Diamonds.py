import pygame
import sys
import random
from game import Game
from strategy import computer_bid

# Initialize Pygame
pygame.init()

# Set up the screen dimensions
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))

# Set the title of the window
pygame.display.set_caption("Diamonds")

# Define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Load card images
card_images = {}
for i in range(2, 15):
    card_path = f"images/{i}_of_diamonds.png"  # Adjust the path as needed
    card_images[i] = pygame.transform.scale(pygame.image.load(card_path), (72, 96))  # Adjust size as needed

# Fonts
font = pygame.font.Font(None, 36)

def draw_text(text, color, x, y):
    text_surface = font.render(text, True, color)
    text_rect = text_surface.get_rect(center=(x, y))
    screen.blit(text_surface, text_rect)

def start_screen():
    screen.fill(WHITE)
    draw_text("Diamonds", BLACK, screen_width // 2, screen_height // 2 - 100)
    pygame.draw.rect(screen, BLACK, (screen_width // 2 - 100, screen_height // 2, 200, 50))
    draw_text("Start Game", WHITE, screen_width // 2, screen_height // 2 + 25)
    pygame.display.flip()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos
                if screen_width // 2 - 100 <= x <= screen_width // 2 + 100 and \
                   screen_height // 2 <= y <= screen_height // 2 + 50:
                    return

def end_screen(player_score, computer_score):
    while True:
        screen.fill(WHITE)
        
        if player_score > computer_score:
            draw_text("You Win!", BLACK, screen_width // 2, screen_height // 2 - 50)
        elif computer_score > player_score:
            draw_text("Computer Wins!", BLACK, screen_width // 2, screen_height // 2 - 50)
        else:
            draw_text("It's a Tie!", BLACK, screen_width // 2, screen_height // 2 - 50)
        
        # Draw 'Play Again' button
        pygame.draw.rect(screen, BLACK, (screen_width // 2 - 100, screen_height // 2, 200, 50))
        draw_text("Play Again", WHITE, screen_width // 2, screen_height // 2 + 25)
        
        # Draw 'Exit' button
        pygame.draw.rect(screen, BLACK, (screen_width // 2 - 100, screen_height // 2 + 100, 200, 50))
        draw_text("Exit", WHITE, screen_width // 2, screen_height // 2 + 125)
        
        pygame.display.flip()
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos
                if screen_width // 2 - 100 <= x <= screen_width // 2 + 100:
                    if screen_height // 2 <= y <= screen_height // 2 + 50:
                        # Play Again button clicked
                        return True
                    elif screen_height // 2 + 100 <= y <= screen_height // 2 + 150:
                        # Exit button clicked
                        pygame.quit()
                        sys.exit()

def initialize_game():
    return Game("Player")

def player_bid(player):
    selected_card = None
    while True:
        screen.fill(WHITE)
        draw_text("Your Hand:", BLACK, screen_width // 2, screen_height // 2 - 200)
        
        # Draw player's hand
        card_width = 72
        card_height = 96
        card_spacing = 20  # Adjust spacing as needed
        row_spacing = 30  # Adjust spacing between rows as needed
        cards_per_row = 7  # Adjust number of cards per row as needed
        for i, card in enumerate(player.hand, start=1):
            row = 0 if i <= cards_per_row else 1
            col = (i - 1) % cards_per_row
            x = col * (card_width + card_spacing) + card_spacing // 2
            y = row * (card_height + row_spacing) + screen_height // 2 - (1.5 * card_height)
            card_image = card_images[card]  # Use the card_images dictionary from your code
            screen.blit(card_image, (x, y))
            
            # Check if the card is clicked
            card_rect = pygame.Rect(x, y, card_width, card_height)
            if card_rect.collidepoint(pygame.mouse.get_pos()):
                pygame.draw.rect(screen, (255, 0, 0), card_rect, 2)
                
                # Check if the card is clicked
                for event in pygame.event.get():
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        selected_card = card
                        return selected_card
        
        pygame.display.flip()

def game_loop():
    start_screen()
    
    while True:
        game = initialize_game()
        player_score, computer_score = game.play_rounds(player_bid, computer_bid)

        if not end_screen(player_score, computer_score):
            break

game_loop()
