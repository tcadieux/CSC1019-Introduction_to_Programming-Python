# Simple pygame program
def install_and_import(package):
    import importlib
    try:
        importlib.import_module(package)
    except ImportError:
        import pip
        pip.main(['install', package])
    finally:
        globals()[package] = importlib.import_module(package)


install_and_import('pygame')
install_and_import('pygame_widgets')

# Import and initialize the pygame library
import pygame
import pygame_widgets

from pygame_widgets.slider import Slider
from pygame_widgets.textbox import TextBox

pygame.init()
win = pygame.display.set_mode((1000, 1000))

red_slider = Slider(win, 100, 100, 300, 50, min=0, max=255, step=1)
red_output = TextBox(win, 450, 100, 75, 50, fontSize=30)

green_slider = Slider(win, 100, 200, 300, 50, min=0, max=255, step=1)
green_output = TextBox(win, 450, 200, 75, 50, fontSize=30)

blue_slider = Slider(win, 100, 300, 300, 50, min=0, max=255, step=1)
blue_output = TextBox(win, 450, 300, 75, 50, fontSize=30)


red_output.disable()  # Act as label instead of textbox
green_output.disable()  # Act as label instead of textbox
blue_output.disable()  # Act as label instead of textbox


run = True
while run:
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            pygame.quit()
            run = False
            quit()
    

    win.fill((red_slider.getValue(), green_slider.getValue(), blue_slider.getValue()))

    red_output.setText(red_slider.getValue())
    green_output.setText(green_slider.getValue())
    blue_output.setText(blue_slider.getValue())


    pygame_widgets.update(events)
    pygame.display.update()




# # Set up the drawing window
# screen = pygame.display.set_mode([500, 500])

# # Run until the user asks to quit
# running = True
# while running:

#     # Did the user click the window close button?
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             running = False

#     # Fill the background with white
#     screen.fill((255, 255, 255))

#     # Draw a solid blue circle in the center
#     pygame.draw.circle(screen, (0, 0, 255), (250, 250), 75)

#     # Flip the display
#     pygame.display.flip()

# # Done! Time to quit.
# pygame.quit()
