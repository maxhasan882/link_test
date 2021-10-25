from math import sqrt


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def get_euclidean_distance_for_point(self, device):
        return sqrt((self.x-device.x)**2 + (self.y-device.y)**2)
