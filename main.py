from render import render
from genetetor import ImageUtils, ImageFormat

if __name__ == "__main__":
    image = render(100000, 5, 100, 1920, 1080)
    ImageUtils.save(image, "/Users/arinashaydeman/4-python-a-ri-sha-sha/fractal.png", ImageFormat.PNG)
