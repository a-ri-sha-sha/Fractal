from fractal import FractalImage
from point import Point

class GammaCorrection():
    def __init__(self, gamma: float):
        self.gamma = gamma

    def process(self, image: FractalImage):
        for y in range(image._height):
            for x in range(image._width):
                pixel = image.Pixel(Point(x, y))
                pixel.r = int((pixel.r / 255) ** self.gamma * 255)
                pixel.g = int((pixel.g / 255) ** self.gamma * 255)
                pixel.b = int((pixel.b / 255) ** self.gamma * 255)
