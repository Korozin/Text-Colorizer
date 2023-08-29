from Classes import TextColorizer

# Initialize the color class
colors = TextColorizer.MAIN()

# Create a radial text gradient using pre-defined escape codes
start_color = colors.vars.LIGHT_YELLOW
stop_color = colors.vars.LIGHT_GREEN
text = "Hello, gradient!"

gradient_text = colors.GRADIENT(start_color, stop_color, text, "radial", "text")
print(gradient_text)

# Create a radial text gradient using rgb values from the CUSTOM() function
start_color = colors.CUSTOM((255, 0, 0))
stop_color = colors.CUSTOM((255, 255, 0))
text = "Hello, gradient!"

gradient_text = colors.GRADIENT(start_color, stop_color, text, "radial", "text")
print(gradient_text)

# Create a radial text gradient using rgb values modified to be bold
start_color = (255, 0, 0)
stop_color = (255, 255, 0)
text = "Hello, gradient!"

gradient_text = colors.GRADIENT(start_color, stop_color, text, "radial", "text", colors.vars.BOLD)
print(gradient_text)
