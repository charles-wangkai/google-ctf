from PIL import Image, ExifTags

img = Image.open('base_decoded_unhexlified.jpg')
img_exif = img.getexif()

with open('exif.evl', 'w') as out_file:
    out_file.write(
        img_exif[next(key for key, value in ExifTags.TAGS.items() if value == 'Artist')])
