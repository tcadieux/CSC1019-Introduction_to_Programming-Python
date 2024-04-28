
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

# print(color_dict["Black"])
# print(color_dict["White"][1])

red_slider = 10
green_slider = 0
blue_slider = 0


def color_pick(color):
    r = color_dict[color][0]
    g = color_dict[color][1]
    b = color_dict[color][2]
    return ([r,g,b])

print(color_pick("Purple"))



