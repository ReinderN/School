from PIL import Image


def save_rgb(boxed_pixels, filename="out.png"):
    """ need docstrings! """
    print('Bestand ', filename, ' opslaan...')
    w, h = get_wh(boxed_pixels)
    im = Image.new("RGB", (w, h), "black")
    px = im.load()
    for r in range(h):
        for c in range(w):
            bp = boxed_pixels[r][c]
            t = tuple(bp)
            px[c, r] = t
    im.save(filename)
    print(filename, "opgeslagen.")


def get_rgb(filename="in.png"):
    """ reads a png file """
    original = Image.open(filename)
    print("Het formaat van de afbeelding is: ")
    print(original.format, original.size, original.mode)
    width, height = original.size
    px = original.load()
    pixel_list = []
    for r in range(height):
        row = []
        for c in range(width):
            row.append(px[c, r][:3])
        pixel_list.append(row)
    return pixel_list


def get_wh(px):
    """ need docstrings! """
    h = len(px)
    w = len(px[0])
    return w, h


def binary_im(s, cols, rows):
    """ need docstrings! """
    px = []
    for row in range(rows):
        row = []
        for col in range(cols):
            c = int(s[row * cols + col]) * 255
            px = [c, c, c]
            row.append(px)
        px.append(row)
    save_rgb(px, 'binary.png')


class PNGImage:
    def __init__(self, width, height):
        """ constructor for PNGImage """
        self.width = width
        self.height = height
        default = (255, 255, 255)
        self.image_data = [
            [default for col in range(width)]
            for row in range(height)
        ]

    def plot_point(self, col, row, rgb=(0, 0, 0)):
        """ plot a single point to a PNGImage """
        # check if rgb is a three-tuple
        if isinstance(rgb, tuple) and len(rgb) == 3:
            pass  # ok
        elif isinstance(rgb, list) and len(rgb) == 3:
            rgb = tuple(rgb)
        else:
            print("De kleur ", rgb, " in plot_point")
            print("was niet in een bekend formaat.")

        # kijk of we binnen de grenzen zijn:
        if 0 <= col < self.width and 0 <= row < self.height:
            self.image_data[row][col] = rgb

        else:
            print("De positie ", col, row, " in plot_point")
            print("was niet binnen de grenzen.")
            return

        return

    def save_file(self, filename="test.png"):
        """ save the object's data to a file """
        # we reverse the rows so that the y direction
        # increases upwards...
        save_rgb(self.image_data[::-1], filename)
