from link_station.link_station import LinkStation
from link_station.device import Device
import json


class Main:
    def __str__(self):
        result = ""
        for data in self.get_link_station_result():
            result += "{}\n".format(data)
        return result

    @staticmethod
    def get_default_data():
        f = open('default_data.json', )
        data = json.load(f)
        link_stations = []
        devices = []
        for link_station in data["link_stations"]:
            link_stations.append(LinkStation(link_station[0], link_station[1], link_station[2]))
        for device in data["devices"]:
            devices.append(Device(device[0], device[1]))
        return link_stations, devices

    def get_link_station_result(self):
        link_stations, devices = self.get_default_data()
        results = []
        for device in devices:
            results.append(device.get_best_link_station(link_stations))

        return results


if __name__ == '__main__':
    print(Main().__str__())
