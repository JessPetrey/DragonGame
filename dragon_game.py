
''' basic structure of the game: 
The game will have a dragon that the player can control. 
The dragon will be able to move left, right, up, and down to avoid obstacles and collect treasures. 
The game will end if the dragon collides with an obstacle or if the dragon reaches the end of the level.
'''
import pygame
import random
import sys


# Initialize pygame
pygame.init()

# Set the dimensions of the game window
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))

# Load the dragon image and get its rect object
dragon_image = pygame.image.load("Dragon.png")
dragon_image = pygame.transform.rotate(dragon_image, 180)
dragon_rect = dragon_image.get_rect()
# resize the dragon image
dragon_image = pygame.transform.scale(dragon_image, (80, 80))
dragon_rect.width, dragon_rect.height = dragon_image.get_size()


# Set the initial position of the dragon
dragon_rect.centerx = screen_width // 2
dragon_rect.bottom = screen_height - 10

# Set the dragon's movement speed
dragon_speed = 3

# Load the treasure image and create a list to store the treasure objects
treasure_image = pygame.image.load("treasures.png")
treasure_rect = treasure_image.get_rect()
treasure_list = []
max_treasures = 5

# resize the treasure image
treasure_image = pygame.transform.scale(treasure_image, (50, 50))
treasure_rect.width, treasure_rect.height = treasure_image.get_size()

# set the score to 0
score = 0

# Game loop
while True:
        # Handle events
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                        pygame.quit()
                        sys.exit()

        # Spawn a new treasure if there are fewer than max_treasures on the screen
        if len(treasure_list) < max_treasures:
                # generate random x and y coordinates for the treasure
                treasure_x = random.randint(0, screen_width - treasure_rect.width)
                treasure_y = random.randint(0, screen_height - treasure_rect.height)
                # create new treasure object at the generated coordinates
                new_treasure_rect = pygame.Rect(treasure_x, treasure_y, treasure_rect.width, treasure_rect.height)
                treasure_list.append(new_treasure_rect)

        # Move the dragon based on keyboard input
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and dragon_rect.left > 0:
                dragon_rect.x -= dragon_speed
        if keys[pygame.K_RIGHT] and dragon_rect.right < screen_width:
                dragon_rect.x += dragon_speed
        if keys[pygame.K_UP] and dragon_rect.top > 0:
                dragon_rect.y -= dragon_speed
        if keys[pygame.K_DOWN] and dragon_rect.bottom < screen_height:
                dragon_rect.y += dragon_speed

        # # add new treasures randomly
        # if random.random() < 0.02:
        #         # create a new treasure object
        #         treasure_rect = treasure_image.get_rect()
        #         treasure_rect.x = random.randint(0, screen_width - treasure_rect.width)
        #         treasure_rect.y = random.randint(0, screen_height - treasure_rect.height)
        #         treasure_list.append(treasure_rect)

        # Check for collisions with treasures
        for treasure_rect in treasure_list:
                if dragon_rect.colliderect(treasure_rect):
                        treasure_list.remove(treasure_rect)
                        score += 1
                        print("You have found a treasure!")

        # Clear the screen
        screen.fill((255, 255, 255))

        # Draw the dragon
        screen.blit(dragon_image, dragon_rect)

        # draw the treasures
        for treasure_rect in treasure_list:
                screen.blit(treasure_image, treasure_rect)

        # update the score
        font = pygame.font.Font(None, 36)
        score_text = font.render("Score: " + str(score), True, (0, 0, 0))
        screen.blit(score_text, (10, 10))

        # Update the screen
        pygame.display.update()