from link_station.point import Point


class Device(Point):

    def format(self, best_station, power):
        if power:
            return "Best link station for point {}, {} is {}, {} with power {}".format(self.x, self.y, best_station.x,
                                                                                       best_station.y, power)
        return "No link station within reach for point {}, {}".format(self.x, self.y)

    def get_best_link_station(self, link_stations):
        best_power = 0
        best_station = link_stations[0]
        for station in link_stations:
            power = station.get_power(self)
            if power > best_power:
                best_station = station
                best_power = power
        return self.format(best_station, best_power)
