import pygame


# Initiate Pygame
pygame.init()

# Screen Settings
SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 728

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
screen.fill("white")
# player = pygame.Rect((300, 250, 50, 50))


# TODO: Load Images
start_img = pygame.image.load('startbutton.jpeg').convert_alpha()
exit_img = pygame.image.load('exitbutton.png').convert_alpha()


# TODO: Button Attributes and Methods
class Button():

    def __init__(self, x, y, image, scale):
        width = image.get_width()
        height = image.get_height()
        self.image = pygame.transform.scale(image, (int(width * scale), int(height * scale)))
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.clicked = False # buttons starts as unclicked

    def draw(self, surface):
        action = False
        # get mouse position
        pos = pygame.mouse.get_pos()

        # check mouseover and clicked conditions
        if self.rect.collidepoint(pos): # is the mouse cursor colliding with mouse button
            if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False: # [0] is left mouse button
                self.clicked = True
                action = True

        if pygame.mouse.get_pressed()[0] == 0:
            self.clicked = False

        # draw button on screen
        surface.blit(self.image, (self.rect.x, self.rect.y))

        return action


# Create button instances
start_button = Button(400, 300, start_img, 0.5) # x and y coordinate, image, scaling of image
exit_button = Button(1100, 0, exit_img, 0.5)
        

# TODO: Game Loop
def play():

    screen.fill("white") # creates an illusion to cover up

    run = True
    while run:

        if start_button.draw(screen): # draws button
            main_menu()
        if exit_button.draw(screen):
            run = False

    # pygame.draw.rect(screen, (255, 0, 0), player)

    # # Controls
    # key = pygame.key.get_pressed()

    # # K_(the key name)
    # # Moves player
    # if key[pygame.K_a] == True:
    #     player.move_ip(-1, 0)
    # elif key[pygame.K_d] == True:
    #     player.move_ip(1, 0)
    # elif key[pygame.K_w] == True:
    #     player.move_ip(0, -1)
    # elif key[pygame.K_s] == True:
    #     player.move_ip(0, 1)

    # event handler
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        pygame.display.update()


# TODO: Click button to change to another screen
def main_menu():

    screen.fill("black")

    run = True
    while run:
        print("Nothing")
        run = False

    # event handler
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    pygame.display.update()


play()
pygame.quit()

# Having Controls and Pressing Buttons

# Button

# Importing Images

# Make a button