########################################################################
# CSC 1019 Final Project
# Last Updated: April 27, 2024
# Description: A simple GUI using pygame to output color codes in RGB format, and then convert to HEX. Additonal features include
########################################################################

# Import and initialize the required libraries
import pygame
import pygame_widgets
import random

from pygame_widgets.slider import Slider
from pygame_widgets.textbox import TextBox
from pygame_widgets.button import Button
from pygame_widgets.dropdown import Dropdown


pygame.init()
pygame.display.set_caption("RGB to HEX Color Tool")


# Funtion to convert (r,g,b) (decimal) to Hex, including leading zeroes
def decimal_to_hex(value):
    return('{:02X}'.format(value))

# Function to set random values for sliders
def set_random_color():
    red_slider.setValue(random.randrange(0,255))
    green_slider.setValue(random.randrange(0,255))
    blue_slider.setValue(random.randrange(0,255))
    
# Function to reset values for sliders (128)
def reset_color():
    red_slider.setValue(128)
    green_slider.setValue(128)
    blue_slider.setValue(128)


def select_color():
    red_slider.setValue(dropdown.getSelected()[0])
    green_slider.setValue(dropdown.getSelected()[1])
    blue_slider.setValue(dropdown.getSelected()[2])
    
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

   
# Define the window dimensions (width, height
win_dimension = 1000
win = pygame.display.set_mode((win_dimension, win_dimension))


# Item Dimensions
padding = 50
slider_height = 20
slider_width = 250
handle_radius  = 15
textbox_width =  75
textbox_height = 40
font_size = 25
color_window_size = (3*padding)+(3*slider_height)-30

# Slider Creation  
red_slider = Slider(win, padding, padding, slider_width, slider_height, min=0, max=255, step=1, handleRadius = handle_radius)

green_slider = Slider(win, padding, (2*padding)+slider_height, slider_width, slider_height, min=0, max=255, step=1, handleRadius = handle_radius)

blue_slider = Slider(win, padding, (3*padding)+(2*slider_height), slider_width, slider_height, min=0, max=255, step=1, handleRadius = handle_radius)


# Slider Output box Creation
red_output = TextBox(win, (2*padding)+slider_width, padding-10, textbox_width, textbox_height, fontSize=font_size)

green_output = TextBox(win, (2*padding)+slider_width, (2*padding)+slider_height-10, textbox_width, textbox_height, fontSize=font_size)

blue_output = TextBox(win, (2*padding)+slider_width, (3*padding)+(2*slider_height)-10, textbox_width, textbox_height, fontSize=font_size)


# Removes the cursers from display boxes
red_output.disable()  
green_output.disable()  
blue_output.disable()  

# Button to call the Random function
random_button = Button(
    win,  # Surface to place button on
    padding,  # X-coordinate of top left corner
    (color_window_size + 2*padding),  # Y-coordinate of top left corner
    slider_width,  # Width
    textbox_height*2,  # Height
    text='Random',  # Text to display
    fontSize=50,  # Size of font
    margin=20,  # Minimum distance between text/image and edge of button
    radius=10,  # Radius of border corners (leave empty for not curved)
    onClick=lambda: set_random_color()  # Function to call when clicked on
)

# Button to call the Reset function
reset_button = Button(
    win,  # Surface to place button on
    padding,  # X-coordinate of top left corner
    (color_window_size + 3*padding) + (textbox_height*2),  # Y-coordinate of top left corner
    slider_width,  # Width
    textbox_height*2,  # Height
    text='Reset',  # Text to display
    fontSize=50,  # Size of font
    margin=20,  # Minimum distance between text/image and edge of button
    radius=10,  # Radius of border corners (leave empty for not curved)
    onClick=lambda: reset_color()  # Function to call when clicked on
)

# Dropdown to select colors from Dict
dropdown = Dropdown(
    win,  # Surface to place button on
    400,  # X-coordinate of top left corner
    (color_window_size + 2*padding),    slider_width,  # Width
    textbox_height*2,  # Height
    name='Select Color: ',
    choices=[
        *color_dict.keys()
    ],
    values=[*color_dict.values()], 
    fontSize=50,  # Size of font
    margin=20,  # Minimum distance between text/image and edge of button
    borderRadius=10, 

)




# Button to Select from drop down
select_button = Button(
    win,  # Surface to place button on
    400,  # X-coordinate of top left corner
    (color_window_size + 3*padding) + (textbox_height*2),  # Y-coordinate of top left corner
    slider_width,  # Width
    textbox_height*2,  # Height
    text='Select',  # Text to display
    fontSize=50,  # Size of font
    margin=20,  # Minimum distance between text/image and edge of button
    radius=10,  # Radius of border corners (leave empty for not curved)
    onClick=select_color  # Function to call when clicked on
)


######### Run the main loop #####################################

run = True
while run:
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            pygame.quit()
            run = False
            quit()
      
# Define the color values based on the position of the sliders      
    red = red_slider.getValue() # 0 - 255
    green = green_slider.getValue()
    blue = blue_slider.getValue()

# Create the lists for color conversions
    color_list = [red, green, blue]
    compliment_list = []
    hex_list = []
    hex_compliment_list = []

    for item in color_list:
        compliment = 255-item
        compliment_list.append(compliment)

    for item in color_list:
        hex = '{:02X}'.format(item)
        hex_list.append(hex)
    
    
    r_hex = decimal_to_hex(red)
    g_hex = decimal_to_hex(green)
    b_hex = decimal_to_hex(blue)
    
    r_complimentary = (255-red) 
    g_complimentary = (255-green)
    b_complimentary = (255-blue)

    win.fill((255, 255, 255)) #color the whole windoe



    input_color_window = pygame.surface.Surface((color_window_size, color_window_size))
    input_fill = pygame.Surface.fill(input_color_window, (red, green, blue))
    
    comp_color_window = pygame.surface.Surface((color_window_size, color_window_size))
    comp_fill = pygame.Surface.fill(comp_color_window, (r_complimentary, g_complimentary, b_complimentary))
    
    
    win.blit(input_color_window, ((3*padding)+slider_width+textbox_width, padding-10))
    win.blit(comp_color_window, ((4*padding)+slider_width+textbox_width+color_window_size, padding-10))


    red_output.setText(red)
    green_output.setText(green)
    blue_output.setText(blue)


    pygame_widgets.update(events)
    pygame.display.update()
    