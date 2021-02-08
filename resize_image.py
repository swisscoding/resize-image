#!/usr/local/bin/python3
# Made by @swisscoding on Instagram

from colored import stylize, fg
from PIL import Image

# decoration
print(stylize("\n---- | Resize image | ----\n", fg("red")))

# class
class Resize:
    def __init__(self, path, file, width, height):
        self.path = path
        self.file = file
        self.width = width
        self.height = height

    # output magic method
    def __repr__(self):
        return self.resize(self.path, self.file, self.width, self.height)

    # methods
    def resize(self, path, f, w, h):
        # open image and resize it
        image = Image.open(f).convert("RGBA").resize((w, h), Image.ANTIALIAS)
        # save resized image
        image.save(f"{path}/resized_image.png", quality=100, subsampling=0)

        return stylize("\nImage resized >>> resized_image.png created\n", fg("red"))

# main execution
if __name__ == "__main__":
    # user interaction
    path = input("Path to image: ")
    filename = input("Filename: ")
    new_width = int(input("New width in px: "))
    new_height = int(input("New height in px: "))

    print(Resize(path, filename, new_width, new_height))
