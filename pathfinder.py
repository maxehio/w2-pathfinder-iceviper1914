from PIL import Image


"""- data we need to find the next step on our path
    -elevation map data
    -current location that the person is"""


def elevation_map():
    with open("elevation_small.txt") as text:
        text = text.readlines()
        split_text = [line.split() for line in text]
        cleaned_list = [[int(num) for num in row] for row in split_text]
        max_list = [max(row) for row in cleaned_list]
        min_list = [min(row) for row in cleaned_list]
        img = Image.new("RGB", (600, 600))
        max_point = (max(max_list))
        print(max_point)
        # min_point = (min(min_list))
        for y, row in enumerate(cleaned_list):
            for x, num in enumerate(row):
                int((num/max_point) * 255)
                img.putpixel((x, y), (num, num, num))
    img.save("path_finder.png")


elevation_map()
