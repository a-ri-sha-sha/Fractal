class Point:
    def __init__(self, x: float, y: float):
        self.x = x
        self.y = y

class RGB():
    def __init__(self, r: int, g: int, b: int):
        self.r = r
        self.g = g
        self.b = b

class Pixel:
    def __init__(self, r: int, g: int, b: int, hit_count: int):
        self.r = r
        self.g = g
        self.b = b
        self.hit_count = hit_count
    
    def Set(self, rgb: RGB):
        self.r = rgb.r
        self.g = rgb.g
        self.b = rgb.b

    def SetAverage(self, rgb: RGB):
        self.r = (self.r + rgb.r) // 2
        self.g = (self.g + rgb.g) // 2
        self.b = (self.b + rgb.b) // 2
 