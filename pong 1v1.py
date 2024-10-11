import pygame
import sys

# Initialize Pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pong Game")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

# Paddle settings
PADDLE_WIDTH, PADDLE_HEIGHT = 15, 100
paddle_speed = 10

# Ball settings
BALL_SIZE = 15
ball_speed_x, ball_speed_y = 5, 5

# Create paddles and ball
left_paddle = pygame.Rect(30, (HEIGHT - PADDLE_HEIGHT) // 2, PADDLE_WIDTH, PADDLE_HEIGHT)
right_paddle = pygame.Rect(WIDTH - 30 - PADDLE_WIDTH, (HEIGHT - PADDLE_HEIGHT) // 2, PADDLE_WIDTH, PADDLE_HEIGHT)
ball = pygame.Rect(WIDTH // 2 - BALL_SIZE // 2, HEIGHT // 2 - BALL_SIZE // 2, BALL_SIZE, BALL_SIZE)

# Score
left_score = 0
right_score = 0
font = pygame.font.Font(None, 74)

# Main game loop
def game_loop():
    global left_score, right_score, ball_speed_x, ball_speed_y
    clock = pygame.time.Clock()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        # Movement
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w] and left_paddle.top > 0:  # Move left paddle up
            left_paddle.y -= paddle_speed
        if keys[pygame.K_s] and left_paddle.bottom < HEIGHT:  # Move left paddle down
            left_paddle.y += paddle_speed
        if keys[pygame.K_UP] and right_paddle.top > 0:  # Move right paddle up
            right_paddle.y -= paddle_speed
        if keys[pygame.K_DOWN] and right_paddle.bottom < HEIGHT:  # Move right paddle down
            right_paddle.y += paddle_speed

        # Move ball
        ball.x += ball_speed_x
        ball.y += ball_speed_y

        # Ball collision with top and bottom
        if ball.top <= 0 or ball.bottom >= HEIGHT:
            ball_speed_y = -ball_speed_y

        # Ball collision with paddles
        if ball.colliderect(left_paddle) or ball.colliderect(right_paddle):
            ball_speed_x = -ball_speed_x

        # Ball out of bounds
        if ball.left <= 0:
            right_score += 1
            reset_ball()
        elif ball.right >= WIDTH:
            left_score += 1
            reset_ball()

        # Draw everything
        screen.fill(BLACK)
        pygame.draw.rect(screen, BLUE, left_paddle)
        pygame.draw.rect(screen, RED, right_paddle)
        pygame.draw.ellipse(screen, WHITE, ball)

        # Draw scores
        left_text = font.render(str(left_score), True, WHITE)
        right_text = font.render(str(right_score), True, WHITE)
        screen.blit(left_text, (WIDTH // 4, 20))
        screen.blit(right_text, (WIDTH * 3 // 4 - right_text.get_width(), 20))

        pygame.display.flip()
        clock.tick(60)

def reset_ball():
    global ball
    ball.x = WIDTH // 2 - BALL_SIZE // 2
    ball.y = HEIGHT // 2 - BALL_SIZE // 2

# Start the game
if __name__ == "__main__":
    game_loop()
