from Classes import TextColorizer

# Initialize the color class
colors = TextColorizer.MAIN()

# Create a radial background gradient using pre-defined escape codes
start_color = colors.vars.LIGHT_RED_BG
stop_color = colors.vars.LIGHT_GREEN
text = "Hello, gradient!"

gradient_text = colors.GRADIENT(start_color, stop_color, text, "radial", "background")
print(gradient_text)

# Create a radial background gradient using rgb values from the CUSTOM() function
start_color = colors.CUSTOM((255, 0, 0))
stop_color = colors.CUSTOM((255, 255, 0))
text = "Hello, gradient!"

gradient_text = colors.GRADIENT(start_color, stop_color, text, "radial", "background")
print(gradient_text)
