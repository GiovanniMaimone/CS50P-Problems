import sys
import os.path
from PIL import Image, ImageOps


def main():
    command_is_valid()
    try:
        before_image = Image.open(sys.argv[1])

    except FileNotFoundError:
        sys.exit("Input does not exist")

    shirt = Image.open("shirt.png")
    size = shirt.size
    muppet_size_right = ImageOps.fit(before_image, size)
    muppet_size_right.paste(shirt, shirt)
    muppet_size_right.save(sys.argv[2])


def command_is_valid():

    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")

    if len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")

    extension1 = os.path.splitext(sys.argv[1])
    extension2 = os.path.splitext(sys.argv[2])

    if extensions(extension1[1]) == False:
        sys.exit("Invalid output")

    if extensions(extension2[1]) == False:
        sys.exit("Invalid output")

    if extension1[1].lower() != extension2[1].lower():
        sys.exit("Input and output have different extensions")


def extensions(extension):
    if extension in [".jpg", ".png", ".jpeg"]:
        return True
    return False


if __name__ == "__main__":
    main()
