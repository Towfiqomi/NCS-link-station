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
        dto = {
            "x" : link_station[0],
            "y" : link_station[1],
            "reach" : link_station[2]
        }
        link_stations.append(dto)

    for device in data["devices"]:
        dto ={
            "x" : device[0],
            "y" : device[1]
        }
        devices.append(dto)
    return {
        "link_stations" : link_stations,
        "devices": devices
    }