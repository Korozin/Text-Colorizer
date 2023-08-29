from Classes import TextColorizer

# Initialize the color class
colors = TextColorizer.MAIN()

# Create a radial text gradient using rgb values modified to be bold
start_color = (255, 0, 0)
stop_color = (255, 255, 0)
text = "Hello, gradient!"

gradient_text = colors.GRADIENT(start_color, stop_color, text, "radial", "text", colors.vars.BOLD)

# Print Centered Gradient
print(colors.CENTER(gradient_text))
