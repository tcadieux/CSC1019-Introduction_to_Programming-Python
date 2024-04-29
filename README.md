#####  CSC 1019: Introduction to Programming (Python)
# Python Color Picker and Converter
Spring 2024: Final Project
### Requirements:
- At least 3 functions that are used throughout the program
- At least 4 different data types used e.g. strings, integers, floats, lists, dictionaries, etc.
- Instructions/documentation that explains what your program is and how to use it
  - Code comments, readme are acceptable


### Summary
A basic UI built with Pygame to select colors using sliders for Red, Green, and Blue values, as well as convert the RGB values to HEX, and display the complimentaty color. Additional features include 'Reset' and 'Random' buttons

## Included Requirements

#### Functions:
- decimal_to_hex(value)
   Converts a decimal value to hex, and formats ti include leading zeros
  
- set_random_color()
   Sets the values of the color picker sliders to a random value. Called when the Random button is pressed

- reset_color()
   Sets the values of the color picker sliders to the initial value (128). Called when the Reset button is pressed

#### Data Types Used

##### Lists  
`color_list = []`  
`compliment_list = []`  
`hex_list = []  `  
`hex_compliment_list = []  `  

##### Intgers  
`slider_height = 20`  
`slider_width = 250`

##### String
`text='Reset'`

#### Dictionary
```
color_dict = {
    "Black": (0,0,0),
    ......
    "Navy": (0,0,128),
    "Purple": (128,0,128),
}
```





## Reference Materials:
In addition to class materials, the following sources were utilized:
- [Pygame](https://www.pygame.org/news) - 
- [Pygame Widgets](https://pygamewidgets.readthedocs.io/en/stable/)
- [RapidTables](https://www.rapidtables.com/web/color/RGB_Color.html) - Web Color Refrences


