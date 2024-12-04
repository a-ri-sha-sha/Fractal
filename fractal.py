from point import Pixel, Point

class FractalImage:
    def __init__(self, width: int, height: int):
        self._width = width
        self._height = height
        self._data = [[Pixel(0, 0, 0, 0) for _ in range(width)] for _ in range(height)]

    @staticmethod
    def Create(width: int, height: int):
        return FractalImage(width, height)

    def Contains(self, point: Point) -> bool:
        return 0 <= point.x < self._width and 0 <= point.y < self._height

    def Pixel(self, point: Point) -> Pixel:
        if self.Contains(point):
            return self._data[point.y][point.x]
        raise ValueError("Coordinates out of bounds")
