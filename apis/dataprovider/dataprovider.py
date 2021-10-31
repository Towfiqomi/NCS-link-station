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
        link_stations.append([link_station[0], link_station[1], link_station[2]])
    for device in data["devices"]:
        devices.append([device[0], device[1]])
    return link_stations, devices