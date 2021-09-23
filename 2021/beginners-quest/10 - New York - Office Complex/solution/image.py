import tkinter
from PIL import Image, ImageTk
import csv
import sys

MAX_WIDTH = 1024


class WidthSelector():
    def __init__(self, path) -> None:
        self.pixels = []
        with open(path) as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            for row in csv_reader:
                self.pixels.append(
                    tuple(map(lambda x: self.convert(float(x)), row[2:5])))

        self.root = tkinter.Tk()
        self.root.geometry('1024x768')
        width_var = tkinter.StringVar(self.root)
        width_var.set(794)
        self.spinner = tkinter.Spinbox(
            self.root, from_=1, to=MAX_WIDTH, command=self.spinbox_callback, textvariable=width_var)
        self.spinner.bind('<Return>', self.spinbox_callback)
        self.spinner.pack()
        self.canvas = tkinter.Canvas(
            self.root, width=MAX_WIDTH, height=MAX_WIDTH)
        self.canvas.pack()
        self.spinbox_callback()

    def run(self):
        self.root.mainloop()

    def convert(self, original_value):
        old_min = -0.43
        old_max = 0.3
        new_max = 255
        new_min = 0
        return int((((original_value - old_min) * (new_max - new_min)) / (old_max - old_min)) + new_min)

    def spinbox_callback(self, event=None):
        width = int(self.spinner.get())
        height = len(self.pixels) // width
        newImage = Image.new("RGB", (width, height))
        newImage.putdata(self.pixels[:width * height])
        self.image = ImageTk.PhotoImage(newImage)
        self.canvas.create_image(400, 400, image=self.image)


if __name__ == "__main__":
    ws = WidthSelector(sys.argv[1])
    ws.run()
