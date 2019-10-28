def colorize(text, color):
    colors = ("cyan", "yellow", "blue", "green", "magenta")
    if type(text) is not str:
        raise TypeError("text must be | str")
    if color not in colors:
        raise ValueError("color is invalid color")
    print(f"Printed text {text} in color {color}")

colorize("Hello", "red")