import csv
from PIL import Image


def convert(original_value):
    old_min = -0.43
    old_max = 0.3
    new_max = 255
    new_min = 0
    return int((((original_value - old_min) * (new_max - new_min)) / (old_max - old_min)) + new_min)


with open('../resources/chall/7.csv') as csv_file:
    values = []
    csv_reader = csv.reader(csv_file, delimiter=',')
    for i, row in enumerate(csv_reader):
        values.append(tuple(map(lambda x: convert(float(x)), row[2:5])))

    size = (795, 500)
    img = Image.new("RGB", size)
    pixels = []
    counter = 0
    for i, row in enumerate(values):
        if len(pixels) == size[0] * size[1]:
            img.putdata(pixels)
            img.show()
            break

        pixels.append((values[i][0], values[i+25][1], values[i+1][2]))

        if i % (795*2) == 0:
            pixels.append((0, 0, 0))
