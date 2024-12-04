from abc import ABC, abstractmethod
from point import Point
from typing import List
import math

class Transformation(ABC):
    @abstractmethod
    def transform(self, point: Point):
        pass
    
class SinusoidalTransformation(Transformation):
    def transform(self, point: Point) -> Point:
        newX = math.sin(point.x)
        newY = math.sin(point.y)
        return Point(newX, newY)

class SphericalTransformation(Transformation):
    def transform(self, point: Point) -> Point:
        x, y = point.x, point.y
        r_squared = x**2 + y**2
        if r_squared == 0:
            return 0, 0
        newX = x / r_squared
        newY = y / r_squared
        return Point(newX, newY)

class PolarTransformation(Transformation):
    def transform(self, point: Point) -> Point:
        x, y = point.x, point.y
        newX = math.atan2(y, x) / math.pi
        newY = math.sqrt(x**2 + y**2) - 1
        return Point(newX, newY)

class HeartTransformation(Transformation):
    def transform(self, point: Point) -> Point:
        x, y = point.x, point.y
        r_squared = x**2 + y**2
        angle = math.atan2(y, x)
        sqrt_r = math.sqrt(r_squared)
        newX = sqrt_r * math.sin(sqrt_r + r_squared * angle)
        newY = -sqrt_r * math.cos(sqrt_r + r_squared * angle)
        return Point(newX, newY)

class DiskTransformation(Transformation):
    def transform(self, point: Point) -> Point:
        x, y = point.x, point.y
        r_squared = x**2 + y**2
        angle = math.atan2(y, x)
        newX = (1 / math.pi) * angle * math.sin(math.pi * math.sqrt(r_squared))
        newY = (1 / math.pi) * angle * math.cos(math.pi * math.sqrt(r_squared))
        return Point(newX, newY)

transformations: List[Transformation] = [
    SinusoidalTransformation(),
    SphericalTransformation(),
    PolarTransformation(),
    HeartTransformation(),
    DiskTransformation(),
]
