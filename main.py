import tkinter as tk
from tkinter.filedialog import askopenfilename
import numpy as np
from PIL import Image


def convert_img_to_ascii():
    brightness_list = r"""$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~i!lI;:,\"^`". """
    brightness_list_2 = "@%#*+=-:. "
    brightness_list_3 = r"""$@B#jft/\[]-_:^". """
    ascii_width = 100
    tk.Tk().withdraw()  # part of the import if you are not using other tkinter functions

    filename = askopenfilename(initialdir=r"C:\Users\Eduard\Pictures",
                               filetypes=[("Images", "*.jpg"), ("Images", "*.jpeg"), ("Images", "*.png")])
    avg_pixel_values = get_pixel_values(filename, ascii_width)
    avg_pixel_values = np.ceil(((len(brightness_list_3) - 1) * avg_pixel_values) / 255)
    avg_pixel_values = avg_pixel_values.astype("int8")
    res_list = []
    for i in range(len(avg_pixel_values)):
        temp_list = [brightness_list_3[avg_pixel_values[i][j]] for j in range(len(avg_pixel_values[0]))]
        res_list.append(temp_list)
    write_to_file(res_list)
    return res_list


def write_to_file(list_of_text):
    with open("output.txt", "w", encoding="utf8") as text_file:
        for i in range(len(list_of_text)):
            text_file.write(" ".join(list_of_text[i]) + "\n")


def get_pixel_values(filename, ascii_width):
    image = Image.open(filename, "r").convert('L')
    image.thumbnail((ascii_width, ascii_width), Image.ANTIALIAS)
    width, height = image.size
    pixel_values = list(image.getdata())
    pixel_values = np.array(pixel_values).reshape((height, width))
    return pixel_values


if __name__ == "__main__":
    res_list = convert_img_to_ascii()
    for i in range(len(res_list)):
        print(" ".join(res_list[i]))
