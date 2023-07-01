from PIL import Image
import binascii

im = Image.open("symatrix.png")
matrix = im.load()

x_len = im.size[0] // 2
y_len = im.size[1]


binary_string = ""
for i in range(0, y_len):
    for j in range(0, x_len):
        base_pixel = matrix[j, i]
        new_pixel = matrix[im.size[0] - 1 - j, i]
        if new_pixel != base_pixel:
            binary_string += str(new_pixel[2] - base_pixel[2])

print("flag:", binascii.unhexlify(hex(int(binary_string, 2))[2:]))
