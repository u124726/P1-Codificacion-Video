from scipy import fft
import subprocess
import sys


# EXERCISE 1
def rgb_to_yuv(rgb_values):
    """ Translate 3 values from RGB model color to YUV
    Args:
        rgb_values: Array of R,G and B values
    """
    y = 0.257 * rgb_values[0] + 0.504 * rgb_values[1] + 0.098 * rgb_values[2] + 16
    u = -0.148 * rgb_values[0] - 0.291 * rgb_values[1] + 0.439 * rgb_values[2] + 128
    v = 0.439 * rgb_values[0] - 0.368 * rgb_values[1] - 0.071 * rgb_values[2] + 128

    return y, u, v


def yuv_to_rgb(yuv_values):
    """ Translate 3 values from YUV model color to RGB
    Args:
        yuv_values: Array of Y,U and V values
    """
    yuv_values[0] -= 16
    yuv_values[1] -= 128
    yuv_values[2] -= 128

    r = 1.164 * yuv_values[0] + 1.596 * yuv_values[2]
    g = 1.164 * yuv_values[0] - 0.392 * yuv_values[1] - 0.813 * yuv_values[2]
    b = 1.164 * yuv_values[0] + 2.017 * yuv_values[1]

    return r, g, b


# RGB and YUV values to be converted
rgb_values = [10, 10, 10]
yuv_values = [24.59, 128.0, 128.0]

# Showing conversions
print(rgb_to_yuv(rgb_values))
print(yuv_to_rgb(yuv_values))


# EXERCISE 2

def resize_image(image_input, image_output, input_width, input_height):
    """ Resize images into lower quality using ffmpeg
        Args:
            image_input: Image to be resized
            image_output: New image resized
            input_width: Width of resized
            input_height: Height of resized
    """
    ffmpeg_resize = [
        'ffmpeg',
        '-i', image_input,
        '-vf', f'scale={input_width}:{input_height}',
        image_output
    ]
    subprocess.run(ffmpeg_resize)


# resize_image('ronaldinho.jpg','/mnt/c/Users/dcabo/PycharmProjects/rgb_yuv/output.jpg', 640, 480)

# EXERCISE 3
def serpentine(input_file):
    """Estimate the sequence of bytes which conform an image and change them to integer values
    Args:
        input_file: JPG Image file to be read
    """
    with open(input_file, "rb") as image_file:
        n_bytes = image_file.read()
        bytes_file = bytearray(n_bytes)
        sys.set_int_max_str_digits(0)
        int_bytes = int.from_bytes(bytes_file, "big")
        print(int_bytes)


# serpentine('output.jpg')


# EXERCISE 4

def bw_image(image_input, image_output, bwimage_output, input_width, input_height):
    """ Resize images into lower quality and change the results to grayscale using ffmpeg
        Args:
            image_input: Image to be converted
            image_output: New image resized
            bwimage_output: New image in grayscale
            input_width: Width of resized
            input_height: Image to be resized
    """
    ffmpeg_resize = [
        'ffmpeg',
        '-i', image_input,
        '-vf', f'scale={input_width}:{input_height}',
        image_output
    ]

    ffmpeg_bw = [
        'ffmpeg',
        '-i', image_input,
        '-vf', f'format=gray',
        bwimage_output
    ]
    subprocess.run(ffmpeg_resize)
    subprocess.run(ffmpeg_bw)


# bw_image('ronaldinho.jpg','/mnt/c/Users/dcabo/PycharmProjects/rgb_yuv/output_.jpg', '/mnt/c/Users/dcabo/PycharmProjects/rgb_yuv/output_bw.jpg', 96, 54)

"""JPEG nos permite comprimir el tamaño del archivo de imagen al 5% de su tamaño original, es decir,
en este caso de dimensiones 1920x1080 a dimensiones 96x54. Podemos observar en los resultados claramente 00
como hay una pérdida muy significativa en la calidad de la imagen al reducir en un 95% el tamaño original."""


# EXERCISE 5
def run_length_encoding(original_data):
    """Apply run-length encoding on a series of bytes given
    Args:
        original_data: Data to be encoded
    """
    encoded_data = []
    count = 0
    for i in range(len(original_data)):
        if original_data[i] == 0:
            count = count + 1
            if original_data[i + 1] != 0:
                encoded_data.append(original_data[i])
                encoded_data.append(count)
        else:
            count = 0
            encoded_data.append((original_data[i]))

    return encoded_data


data = [17, 8, 54, 0, 0, 0, 97, 5, 16, 0, 45, 23, 0, 0, 0, 0, 0, 3, 67, 0, 8]
print(run_length_encoding(data))


# EXERCISE 6
def dct_transform(input_data):
    """Apply discrete cosine transform (DCT) to input data given
    Args:
        input_data: Data to be converted
    """
    dct_data = fft.dct(input_data)

    return dct_data


print(dct_transform(data))
