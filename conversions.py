import random

red = random.randint(0,255)
green = random.randint(0,255)
blue = random.randint(0,255)


def random_color():
    return random.randint(0,255), random.randint(0,255), random.randint(0,255)





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
    
    
# for comp in color_list: # need to convert to hex
    # compli = 255-comp
    # hex_compliment = '{:02X}'.format(comp)
    # hex_compliment_list.append(hex_compliment)

r = 0
g = 1
b = 2

# print(color_list[r], color_list[g], color_list[b]) 
# print(compliment_list[r]) 

# print(color_list[r] + compliment_list[r])
print(color_list[r])
print(compliment_list[r])
print(hex_list[r])
# print(hex_compliment_list[0])


