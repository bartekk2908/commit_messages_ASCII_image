from os import environ
from PIL import Image


BLACK = chr(9608)   # █
D_GREY = chr(9619)  # ▓
L_GREY = chr(9618)  # ▒
WHITE = chr(9617)   # ░

ASCII_CHARS = (WHITE, L_GREY, D_GREY, BLACK)


def resize_image(image, new_width=100):
    width, height = image.size
    ratio = height / width
    new_height = int(new_width * ratio)
    resized_image = image.resize((new_width, new_height))
    return (resized_image)


def grayify(image):
    grayscale_image = image.convert("L")
    return (grayscale_image)


def pixels_to_ascii(image):
    pixels = image.getdata()
    characters = "".join([ASCII_CHARS[(pixel + 40) // 85] for pixel in pixels])
    return (characters)


if __name__ == "__main__":
    path = "image.png"
    image = Image.open(path)

    new_width = 46

    # convert image to ascii
    new_image_data = pixels_to_ascii(grayify(resize_image(image, new_width)))

    # format
    pixel_count = len(new_image_data)
    ascii_image = "\n".join([new_image_data[index:(index + new_width)] for index in range(0, pixel_count, new_width)])

    # print result
    print(ascii_image)

    # save result to "ascii_image.txt"
    with open("ascii_art.txt", "w", encoding="utf-8") as f:
        f.write(ascii_image)
