# Text-Colorizer

A simple Python class to colorize text.

# Function Overview

### COMBINE
Takes as many ANSI codes (both custom and pre-defined), and merges them into a single variable

### CUSTOM
Takes either an `rgb()` value or a hex color string as input and returns it as a custom ANSI color code.

### CENTER
Centers text across your Terminal's X-Axis using `shutil`

### GRADIENT
Takes 2 color inputs:
* `start_color`
* `stop_color`

Valid input types are `rgb()`, hex color code, or pre-defined ANSI color code.

(Note: pre-defined ANSI color codes were an afterthought for this function, so it was just kinda thrown in and the colors are statically defined per ANSI code. If you don't like that rigidity, use a custom rgb or hex value)

Takes 1 text input:
* `text` which is the text that will be returned

Takes 3 typing inputs:
* `gradient_type` which can be either `linear` or `radial`
* `text_mode` which can be either `text` or `background`
* `modifiers` which can take an ANSI code such as `BOLD` or `BLINK`

### RAINBOW
Basically the same as `GRADIENT`, except instead of passing colors yourself, it automatically returns it as a rainbow.
