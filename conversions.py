# Function to write RGB in format r,g,b
def printLabel(): 
    print(f'rgb({r},{g},{b})   hex: {r_hex}{g_hex}{b_hex}')

# Funtion to convert (r,g,b) (decimal) to Hex, including leading zeroes
def decimal_to_hex(value):
    return('{:02X}'.format(value))

