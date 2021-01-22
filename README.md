# Image to ASCII art converter
Python script for converting any picture into an ASCII art picture.

![alt text](https://github.com/alvarogharo/image-to-ascii-art/blob/main/examples/face.jpg)

![alt text](https://github.com/alvarogharo/image-to-ascii-art/blob/main/examples/face-ascii.jpg)

## Installation
```pip3 install -r requirements.txt```

## Launch
```python3 image-to-ascci.py -i ./google.jpg -o ./a.jpg -s 0.3 -c 0 0 255 -m True```

## Config parameters
| Argument | Abbreviation | Description |
| -- | -- | -- |
| --inputimage | -i | Path to the image to ve converted |
| --outputpath | -o | Path where the output image is going to be stored |
| --scale | -s | The scale in which the image is going to ve resized (from 0.01 to 1) |
| --monochrome | -m | If True the image characters will be of only one color, this color can be defined with --color. By default set to False |
| --color | -c | Color for the characters of the picture in RGB. For this to work you should also declare --monochrome True |

