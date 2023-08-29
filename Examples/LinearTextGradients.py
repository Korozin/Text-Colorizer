from Classes import TextColorizer

# Initialize the color class
colors = TextColorizer.MAIN()

# Create a linear text gradient using hex codes
start_color = "#ff0000"
stop_color = "#0000ff"
text = "Hello, gradient!"

gradient_text = colors.GRADIENT(start_color, stop_color, text, "linear", "text")
print(gradient_text)

# Create a linear text gradient using rgb values
start_color = (0, 255, 0)
stop_color = (0, 255, 255)
text = "Hello, gradient!"

gradient_text = colors.GRADIENT(start_color, stop_color, text, "linear", "text")
print(gradient_text)

# Create a linear text gradient using rgb values modified to be bold
start_color = (255, 0, 0)
stop_color = (255, 255, 0)
text = "Hello, gradient!"

gradient_text = colors.GRADIENT(start_color, stop_color, text, "linear", "text", colors.vars.BOLD)
print(gradient_text)
