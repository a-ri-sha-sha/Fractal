from enum import Enum
from PIL import Image
from fractal import FractalImage
from point import Point

class ImageFormat(Enum):
    JPEG = "jpeg"
    BMP = "bmp"
    PNG = "png"

class ImageUtils:
    @staticmethod
    def save(image: FractalImage, filename: str, format: ImageFormat):
        pil_image = Image.new("RGB", (image._width, image._height))
        for y in range(image._height):
            for x in range(image._width):
                pixel = image.Pixel(Point(x, y))
                pil_image.putpixel((x, y), (pixel.r, pixel.g, pixel.b))
        pil_image.save(filename, format.value)
