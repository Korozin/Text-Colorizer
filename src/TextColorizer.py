import re, shutil


class ANSIColors:
    def __init__(self):
        # Define codes to vars
        self.__define()
        self.__begin()


    def __define(self):
        # Reset all formatting
        self.RESET = 0

        # Text Colors #
        self.BLACK = 30
        self.RED = 31
        self.GREEN = 32
        self.YELLOW = 33
        self.BLUE = 34
        self.MAGENTA = 35
        self.CYAN = 36
        self.WHITE = 37
        self.GRAY = 90
        # Light Text Colors #
        self.LIGHT_RED = 91
        self.LIGHT_GREEN = 92
        self.LIGHT_YELLOW = 93
        self.LIGHT_BLUE = 94
        self.LIGHT_MAGENTA = 95
        self.LIGHT_CYAN = 96

        # Background Colors #
        self.DEFAULT_BG = 49
        self.BLACK_BG = 40
        self.RED_BG = 41
        self.GREEN_BG = 42
        self.YELLOW_BG = 43
        self.BLUE_BG = 44
        self.MAGENTA_BG = 45
        self.CYAN_BG = 46
        self.WHITE_BG = 47
        self.GRAY_BG = 100
        # Light Background Colors #
        self.LIGHT_RED_BG = 101
        self.LIGHT_GREEN_BG = 102
        self.LIGHT_YELLOW_BG = 103
        self.LIGHT_BLUE_BG = 104
        self.LIGHT_MAGENTA_BG = 105
        self.LIGHT_CYAN_BG = 106

        # Text Effects #
        self.BOLD = 1
        self.UNDERLINE = 4
        self.DIM = 2
        self.BLINK = 5
        self.REVERSE = 7
        self.HIDDEN = 8


    def __begin(self):
        for attr_name in dir(self):
            if not attr_name.startswith("__"):  # Exclude built-in attributes
                code = getattr(self, attr_name)
                if isinstance(code, int):
                    setattr(self, attr_name, "\033[" + str(code) + "m")



class MAIN:
    def __init__(self):
        self.vars = ANSIColors()


    def COMBINE(self, *colors):
        combined = ''.join(colors)
        return combined


    def CUSTOM(self, color):
        if isinstance(color, tuple) and len(color) == 3:
            # RGB values
            r, g, b = color
            return f"\033[38;2;{r};{g};{b}m"
        elif isinstance(color, str):
            color = color.strip("#")
            if len(color) == 6:
                # Hex color code
                r, g, b = int(color[:2], 16), int(color[2:4], 16), int(color[4:], 16)
                return f"\033[38;2;{r};{g};{b}m"
        raise ValueError("Invalid color format. Please provide RGB values as a tuple or hex color code as a string.")


    def CENTER(self, text):
        terminal_width = shutil.get_terminal_size().columns
        ansi_escape = re.compile(r'\x1B(?:[@-Z\\-_]|\[[0-?]*[ -/]*[@-~])')
        plain_text = ansi_escape.sub('', text)
        padding = (terminal_width - len(plain_text)) // 2
        centered_text = ' ' * padding + text
        return centered_text


    def GRADIENT(self, start_color, stop_color, text, gradient_type="linear", text_mode="text", modifiers=None):
        def __ansi_to_rgb(code):
            color_map = {30: (0, 0, 0), 31: (255, 0, 0), 32: (0, 255, 0), 33: (255, 255, 0), 34: (0, 0, 255), 35: (255, 0, 255), 36: (0, 255, 255), 37: (255, 255, 255), 90: (128, 128, 128), 91: (255, 128, 128), 92: (128, 255, 128), 93: (255, 255, 128), 94: (128, 128, 255), 95: (255, 128, 255), 96: (128, 255, 255), 40: (0, 0, 0), 41: (255, 0, 0), 42: (0, 255, 0), 43: (255, 255, 0), 44: (0, 0, 255), 45: (255, 0, 255), 46: (0, 255, 255), 47: (255, 255, 255), 100: (128, 128, 128), 101: (255, 128, 128), 102: (128, 255, 128), 103: (255, 255, 128), 104: (128, 128, 255), 105: (255, 128, 255), 106: (128, 255, 255)}
            color = color_map.get(code, None)
            if color:
                return color
            else:
                raise ValueError("Unknown ANSI Code! Are you sure you're using a valid one?")

        def __parse_color(color):
            if isinstance(color, str):
                if color.startswith("#"):
                    hex_value = color[1:]
                    if len(hex_value) == 3:
                        hex_value = "".join(c * 2 for c in hex_value)
                    if len(hex_value) == 6:
                        r = int(hex_value[0:2], 16)
                        g = int(hex_value[2:4], 16)
                        b = int(hex_value[4:6], 16)
                        return r, g, b
                elif color.startswith("\033[38;2;"):
                    color = color.split(';')[2:5]
                    color = tuple(int(value.replace("m", "")) for value in color)
                    return color
                elif color.startswith("\033["):
                    color = color[2:-1]
                    color = __ansi_to_rgb(int(color))
                    return color
            elif isinstance(color, tuple) and len(color) == 3:
                return color
            raise ValueError("Invalid color format. Please provide colors as RGB tuples, or hex color codes (e.g., (255, 0, 0), '#RRGGBB')")

        start_color, stop_color = __parse_color(start_color), __parse_color(stop_color)

        gradient = ""
        text_length = len(text)
        for i, char in enumerate(text):
            if gradient_type == "linear":
                ratio = i / max(1, text_length - 1)
            elif gradient_type == "radial":
                # Calculate the distance from the center
                distance = abs(i - text_length // 2)
                max_distance = text_length // 2

                # Calculate the ratio based on the distance
                ratio = distance / max(1, max_distance)
            else:
                raise ValueError("Invalid gradient type. Please choose 'linear' or 'radial'.")

            if isinstance(start_color, tuple) and isinstance(stop_color, tuple):
                r = int(start_color[0] + ratio * (stop_color[0] - start_color[0]))
                g = int(start_color[1] + ratio * (stop_color[1] - start_color[1]))
                b = int(start_color[2] + ratio * (stop_color[2] - start_color[2]))
                if text_mode == "text":
                    color_code = f"\033[38;2;{r};{g};{b}m{char}"
                elif text_mode == "background":
                    color_code = f"\033[48;2;{r};{g};{b}m{char}"
                else:
                    raise ValueError("Invalid Gradient Display mode! Must be 'text' or 'background'!")

            if modifiers:
                gradient += str(modifiers) + color_code + self.vars.RESET
            else:
                gradient += color_code + self.vars.RESET

        return gradient


    def RAINBOW(self, text, gradient_type="linear", text_mode="text", modifiers=None):
        rainbow_colors = ((255, 0, 0), (255, 63, 0), (255, 95, 0), (255, 127, 0), (255, 159, 0), (255, 191, 0), (255, 223, 0), (255, 255, 0), (223, 255, 0), (191, 255, 0), (159, 255, 0), (127, 255, 0), (95, 255, 0), (63, 255, 0), (31, 255, 0), (0, 255, 0), (0, 223, 31), (0, 191, 63), (0, 159, 95), (0, 127, 127), (0, 95, 159), (0, 63, 191), (0, 31, 223), (0, 0, 255), (31, 0, 223), (63, 0, 191), (95, 0, 159), (127, 0, 127), (159, 0, 95), (191, 0, 63), (223, 0, 31), (255, 0, 0), (255, 63, 0), (255, 95, 0), (255, 127, 0), (255, 159, 0), (255, 191, 0), (255, 223, 0))

        def __parse_color(color):
            if isinstance(color, tuple) and len(color) == 3:
                return color
            else:
                raise ValueError("Invalid color format. Please provide a tuple of (R, G, B) values or a valid string format.")

        gradient = ""
        text_length = len(text)
        num_colors = len(rainbow_colors)

        for i, char in enumerate(text):
            if gradient_type == "linear":
                ratio = i / max(1, text_length - 1)
            elif gradient_type == "radial":
                # Calculate the distance from the center
                distance = abs(i - text_length // 2)
                max_distance = text_length // 2

                # Calculate the ratio based on the distance
                ratio = distance / max(1, max_distance)
            else:
                raise ValueError("Invalid gradient type. Please choose 'linear' or 'radial'.")

            # Calculate the start and stop colors for the current position
            start_index = int(ratio * (num_colors - 1))
            stop_index = start_index + 1

            if stop_index >= num_colors:
                stop_index = num_colors - 1

            start_color = rainbow_colors[start_index]
            stop_color = rainbow_colors[stop_index]

            r = int(start_color[0] + ratio * (stop_color[0] - start_color[0]))
            g = int(start_color[1] + ratio * (stop_color[1] - start_color[1]))
            b = int(start_color[2] + ratio * (stop_color[2] - start_color[2]))

            if text_mode == "text":
                color_code = f"\033[38;2;{r};{g};{b}m{char}"
            elif text_mode == "background":
                color_code = f"\033[48;2;{r};{g};{b}m{char}"
            else:
                raise ValueError("Invalid Gradient Display mode! Must be 'text' or 'background'!")

            if modifiers:
                gradient += str(modifiers) + color_code + self.vars.RESET
            else:
                gradient += color_code + self.vars.RESET

        return gradient
