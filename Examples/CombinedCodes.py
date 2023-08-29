from Classes import TextColorizer

# Initialize the color class
colors = TextColorizer.MAIN()

# Access combined color variables using pre-defined escape codes
red_blink = colors.COMBINE(colors.vars.BOLD, colors.vars.BLINK, colors.vars.LIGHT_CYAN)
print(red_blink + "Hello, Color!" + colors.vars.RESET)

# Create a radial text gradient using rgb values modified to be both bold and blinking
start_color = (255, 0, 0)
stop_color = (255, 255, 0)
text = "Hello, gradient!"
codes = colors.COMBINE(colors.vars.BLINK, colors.vars.BOLD)

gradient_text = colors.GRADIENT(start_color, stop_color, text, "radial", "text", codes)
print(gradient_text)
