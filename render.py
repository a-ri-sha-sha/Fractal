from fractal import FractalImage
from point import Point, RGB
from image_processor import GammaCorrection
from transformation import Transformation
from typing import List
import random

class AffineTransformation:
    def __init__(self):
        self.a = random.uniform(-1, 1)
        self.b = random.uniform(-1, 1)
        self.c = random.uniform(-1, 1)
        self.d = random.uniform(-1, 1)
        self.e = random.uniform(-1, 1)
        self.f = random.uniform(-1, 1)
        self.rgb = RGB(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

    def apply(self, point: Point) -> Point:
        newX = self.a * point.x + self.b * point.y + self.c
        newY = self.d * point.x + self.e * point.y + self.f
        return Point(newX, newY)

XMIN, XMAX = -1.777, 1.777
YMIN, YMAX = -1, 1

def is_valid_point(point: Point) -> bool:
    return XMIN <= point.x <= XMAX and YMIN <= point.y <= YMAX

def make_new_point(point: Point,  width: int, height: int) -> Point:
    x1 = int(width - ((XMAX - point.x) / (XMAX - XMIN)) * width)
    y1 = int(height - ((YMAX - point.y) / (YMAX - YMIN)) * height)
    return Point(x1, y1)

def render(n: int, eq_count: int, it : int, width: int, height: int, transformations: List[Transformation]) -> FractalImage:
    coeffs = [AffineTransformation() for _ in range(eq_count)]

    image = FractalImage.Create(width, height)
    correction = GammaCorrection(2.2)
    for _ in range(n):
        new_point = Point(random.uniform(XMIN, XMAX), random.uniform(YMIN, YMAX))
        for step in range(-20, it):
            i = random.randint(0, eq_count - 1)
            coeff = coeffs[i]
            point = coeff.apply(new_point)
            transformation = random.choice(transformations)
            new_point = transformation.transform(point)
            if step >= 0 and is_valid_point(new_point):
                point1 = make_new_point(new_point, width, height)
                if image.Contains(point1):
                    pixel = image.Pixel(point1)
                    if pixel.hit_count == 0:
                        pixel.Set(coeff.rgb)
                    else:
                        pixel.SetAverage(coeff.rgb)
                    pixel.hit_count += 1
    correction.process(image)
    return image
