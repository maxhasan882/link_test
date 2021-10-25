from link_station.point import Point


class LinkStation(Point):

    def __init__(self, x, y, reach):
        super().__init__(x, y)
        self.reach = reach

    def get_power(self, device):
        distance = Point(self.x, self.y).get_euclidean_distance_for_point(device)
        return (self.reach - distance)**2 if distance < self.reach else 0
