import pygame

run = True #program will run as long as run variable is True
width = 400 #width of screen
height = 100 #height of screen
pygame.init() #initialize the pygame environment
screen = pygame.display.set_mode((width, height)) #prepare application window
font = pygame.font.SysFont(None, 48) #make an object representing the default font os size 48 points;
text = font.render("Welcome to pygame", True, (255, 255, 255)) # make an object representing a given text => text will be anti-aliased(True) and white (255,255,255)
screen.blit(text, ((width - text.get_width()) // 2, (height - text.get_height()) // 2)) # insert the text into the (currently invisible) screen buffer
pygame.display.flip() # flip the screen buffers to make the text visible
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT\
        or event.type == pygame.MOUSEBUTTONUP\
        or event.type == pygame.KEYUP:
            run = False