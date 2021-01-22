import cv2
import numpy as np
import argparse


def generate_lines_ascii_array_from_image(image_path, scale_down_ratio=0.3):
    color_levels = list(reversed("$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,\"^`'. "))
    color_levels_count = len(color_levels)
    aspect_ratio = 3.846 / 3
    
    image = cv2.imread(image_path)
    dim = (int(image.shape[1] * scale_down_ratio), int(image.shape[0] * (scale_down_ratio / aspect_ratio)))

    image_color = cv2.resize(image, dim)

    image_grey = cv2.cvtColor(image_color, cv2.COLOR_BGR2GRAY)
    coded_image = np.array((image_grey / 255) * 70, dtype=np.int)
    final_image = np.empty(image_grey.shape, dtype="object")

    for i in range(color_levels_count):
        character = color_levels[i]
        final_image = np.where(coded_image == i, character, final_image)
    final_image = np.where(coded_image == 70, color_levels[len(color_levels)-1], final_image)

    image_in_lines = []
    for i in range(final_image.shape[0]):
        line = ""
        for j in range(final_image.shape[1]):
            line += final_image[i, j]
        image_in_lines.append(line)

    return image_in_lines, image_color


def generate_image_from_lines_array(lines, colors, out_path, font_col=None, monocrome=False):
    horizontal_init = 15
    vertical_init = 30
    horizontal_gap = 14
    vertical_gap = 18
    vertical_margin = 25
    horizontal_margin = 30

    image = np.zeros((len(lines) * vertical_gap + vertical_margin, len(lines[0]) * horizontal_gap + horizontal_margin, 3), np.uint8)

    font = cv2.FONT_ITALIC
    position = (horizontal_init, vertical_init)
    font_scale = 0.7
    font_color = (255, 0, 0)
    if font_col is not None:
        font_color = (int(font_col[2]), int(font_col[1]), int(font_col[0]))
    line_type = 2

    for i in range(len(lines)):
        for j in range(len(lines[i])):
            if not monocrome:
                font_color = (int(colors[i][j][0]), int(colors[i][j][1]), int(colors[i][j][2]))
            cv2.putText(image, lines[i][j], position, font, font_scale, font_color, line_type)
            position = (position[0] + horizontal_gap, position[1])
        position = (horizontal_init, position[1] + vertical_gap)

    cv2.imwrite(out_path, image)

    return image


if __name__ == '__main__':
    ap = argparse.ArgumentParser()
    ap.add_argument("-i", "--inputimage", required=True, help="Path to the image to ve converted")
    ap.add_argument("-o", "--outputpath", required=True, help="Path where the output image is going to be stored")
    ap.add_argument("-s", "--scale", required=False, type=float, help="The scale in which the image is going to ve "
                                                                      "resized (from 0.01 to 1)")
    ap.add_argument('-c', '--color', nargs='+', help='Color for the ascii character in rgb', required=False)
    ap.add_argument('-m', '--monocrome', help='True if you want the picture to only be created with monocrome'
                                                         ' characters', required=False)
    args = vars(ap.parse_args())

    input_path = args["inputimage"]
    output_path = args["outputpath"]
    scale = 0.3
    if args["scale"] is not None:
        scale = args["scale"]
    color = args["color"]
    monocrome = False
    if args["monocrome"] is not None:
        monocrome = args["monocrome"] == "True"


    image_lines, image_color = generate_lines_ascii_array_from_image(input_path, scale)
    generate_image_from_lines_array(image_lines, image_color, output_path, color, monocrome)


