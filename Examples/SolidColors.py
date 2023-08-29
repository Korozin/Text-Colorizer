from Classes import TextColorizer

# Initialize the color class
colors = TextColorizer.MAIN()

# Access color variables using pre-defined escape code
print(colors.vars.LIGHT_RED + "Hello, Color!" + colors.vars.RESET)

# Access color variables using RGB values
print(colors.CUSTOM((255, 0, 255)) + "Hello, Color!" + colors.vars.RESET)

# Access color variables using hex color code
print(colors.CUSTOM("#7f395f") + "Hello, Color!" + colors.vars.RESET)
