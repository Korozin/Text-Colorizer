from Classes import TextColorizer

# Initialize the color class
colors = TextColorizer.MAIN()

# Create a radial text rainbow gradient modified to be bold
text = "Hello, Rainbow!"

gradient_text = colors.RAINBOW(text, "radial", "text", colors.vars.BOLD)
print(gradient_text)
