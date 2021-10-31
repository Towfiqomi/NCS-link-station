import json
import os
from apis.dtos import dtos
dir_path = os.path.dirname(os.path.realpath(__file__))


def read_datafile():
    with open(dir_path + "/" + "data.json") as dataFile:
        return json.load(dataFile)


def get_data():
    data = read_datafile()
    link_stations = []
    devices = []
    for link_station in data["link_stations"]:
        list_link_station = dtos.LinkStation(
            x = link_station[0],
            y = link_station[1],
            reach = link_station[2]
        )
        link_stations.append(list_link_station)

    for device in data["devices"]:
        list_device =dtos.Device(
            x = device[0],
            y = device[1]
        )
        devices.append(list_device)
    return {
        "link_stations" : link_stations,
        "devices": devices
    }