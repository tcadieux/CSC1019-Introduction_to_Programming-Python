
# Import and initialize the pygame & pygame_widgets libraries

import pygame
import pygame_widgets
import random

from pygame_widgets.slider import Slider
from pygame_widgets.textbox import TextBox


pygame.init()

 # Function to write RGB in format r,g,b
def printLabel(): 
    print(f'rgb({r},{g},{b})   hex: {r_hex}{g_hex}{b_hex},   compliment rgb({r_complimentary},{b_complimentary},{g_complimentary})')

# Funtion to convert (r,g,b) (decimal) to Hex, including leading zeroes
def decimal_to_hex(value):
    return('{:02X}'.format(value))

# Define the window dimensions (width, height
win_dimension = 1000
margin = win_dimension / 20

win = pygame.display.set_mode((win_dimension, win_dimension))

r_random = random.randrange(0,255)
g_random = random.randrange(0,255)
b_random = random.randrange(0,255)


red_slider = Slider(win, 100, 100, 300, 25, min=0, max=255, step=1)
red_output = TextBox(win, 450, 100, 75, 50, fontSize=30)
red_hex_output = TextBox(win, 550, 100, 75, 50, fontSize=30)

green_slider = Slider(win, 100, 200, 300, 25, min=0, max=255, step=1)
green_output = TextBox(win, 450, 200, 75, 50, fontSize=30)
green_hex_output = TextBox(win, 550, 200, 75, 50, fontSize=30)

blue_slider = Slider(win, 100, 300, 300, 25, min=0, max=255, step=1)
blue_output = TextBox(win, 450, 300, 75, 50, fontSize=30)
blue_hex_output = TextBox(win, 550, 300, 75, 50, fontSize=30)





# Removes the cursers from display box  
red_output.disable()  
green_output.disable()  
blue_output.disable()  



run = True
while run:
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            pygame.quit()
            run = False
            quit()
            
    r = red_slider.getValue() # in rgb
    g = green_slider.getValue()
    b = blue_slider.getValue()
    
    
    r_hex = decimal_to_hex(r)
    g_hex = decimal_to_hex(g)
    b_hex = decimal_to_hex(b)
    
    r_complimentary = (255-r) 
    g_complimentary = (255-g)
    b_complimentary = (255-b)

    win.fill((255, 255, 255)) #color the whole windoe


    input_color_window = pygame.surface.Surface((150, 150))
    input_fill = pygame.Surface.fill(input_color_window, (r, g, b))
    
    comp_color_window = pygame.surface.Surface((150, 150))
    comp_fill = pygame.Surface.fill(comp_color_window, (r_complimentary, g_complimentary, b_complimentary))
    
    rand_color_window = pygame.surface.Surface((150, 150))
    rand_fill = pygame.Surface.fill(rand_color_window, (r_random, g_random, b_random))
    
    win.blit(input_color_window, (150, 400))
    win.blit(comp_color_window, (150, 200))
    win.blit(rand_color_window, (150, 0))




    red_output.setText(r)
    green_output.setText(g)
    blue_output.setText(b)
    red_hex_output.setText(r_hex)
    green_hex_output.setText(g_hex)
    blue_hex_output.setText(b_hex)
    
    
    
   
   
    # printLabel() 
    # decimal_to_hex(r)


    pygame_widgets.update(events)
    pygame.display.update()
    