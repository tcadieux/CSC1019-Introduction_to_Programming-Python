import pygame_widgets
import pygame
from pygame_widgets.button import Button
from pygame_widgets.dropdown import Dropdown

pygame.init()
win = pygame.display.set_mode((400, 280))



color_dict = {
    "Black": (0,0,0),
    "White": (255,255,255),
    "Red": (255,0,0),
    "Green": (0,255,0),
    "Blue": (0,0,255),
    "Yellow": (255,255,0),
    "Cyan": (0,255,255),
    "Magenta": (255,0,255),
    "Navy": (0,0,128),
    "Purple": (128,0,128),
}

def print_value():
    print(dropdown.getSelected())

dropdown = Dropdown(
    win, 120, 10, 100, 50, name='Select Color',
    choices=[
        *color_dict.keys()
    ],
    borderRadius=3, 
    colour=pygame.Color('grey'), 
    values=[*color_dict.values()], 
    direction='down', 
    textHAlign='left'
)

button = Button(
    win, 10, 10, 100, 50, text='Print Value', fontSize=30,
    margin=20, inactiveColour=(255, 0, 0), pressedColour=(0, 255, 0),
    radius=5, onClick=print_value, font=pygame.font.SysFont('calibri', 10),
    textVAlign='bottom'
)

run = True
while run:
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            pygame.quit()
            run = False
            quit()

    win.fill((255, 255, 255))

    pygame_widgets.update(events)
    pygame.display.update()