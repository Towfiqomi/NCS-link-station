import json
import os
from apis.dtos import dtos

dir_path = os.path.dirname(os.path.realpath(__file__))


def read_datafile():
    """Opens the data.json file the same directory and retruns the data in JSON format

    dir_path :
        referes to the dir_path varaible returns the current directory of the file
    """
    with open(dir_path + "/" + "data.json") as dataFile:
        return json.load(dataFile)


def get_data():
    """Receives the data and and converts the data in dtos.DataEntity key value pair format

    #Return:
        A list of dtos.DataEntity fomatted data consisting of dicts of linkstations and points
    """
    data = read_datafile()
    link_stations = []
    points = []

    for link_station in data["link_stations"]:
        list_link_station = dtos.LinkStation(
            x=link_station[0], y=link_station[1], reach=link_station[2]
        )
        link_stations.append(list_link_station)

    for point in data["points"]:
        list_point = dtos.Point(x=point[0], y=point[1])
        points.append(list_point)
    return dtos.DataEntity(link_stations=link_stations, points=points)

#  [100, 100],
#  [15, 10],
#  [18, 18]