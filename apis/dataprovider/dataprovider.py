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
    points = []

    for link_station in data["link_stations"]:
        list_link_station = dtos.LinkStation(
            x=link_station[0], y=link_station[1], reach=link_station[2]
        )
        link_stations.append(list_link_station)

    for point in data["points"]:
        list_device = dtos.Point(x=point[0], y=point[1])
        points.append(list_device)
    return dtos.DataEntity(link_stations=link_stations, points=points)
