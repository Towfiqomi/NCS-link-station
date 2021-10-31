import json
import math
from apis.dtos import dtos
from apis.dataprovider import dataprovider

def get_euclidean_distance_for_point(point : dtos.Point):
    return math.sqrt((point.x)**2 + (point.y)**2)


def get_power(linkstation : dtos.LinkStation, point : dtos.Point):
    distance = get_euclidean_distance_for_point(point)
    power = (linkstation.reach - distance)**2 if distance < linkstation.reach else 0
    return power

def format(power, best_station : dtos.LinkStation, point : dtos.Point):
    if power:
        return "Best link station for point {}, {} is {}, {} with power {}".format(point.x, point.y, best_station.x,
                                                                                       best_station.y, power)
    return "No link station within reach for point {}, {}".format(point.x, point.y)

def get_best_station(data_entity : dtos.DataEntity):
    best_power = 0
    best_station = dtos.LinkStation
    point = dtos.Point
    for station in range(len(data_entity.link_stations)):
        for point_index in range(len(data_entity.points)):
            power = get_power(data_entity.link_stations[station], data_entity.points[point_index])
            if power > best_power:
                best_power = power
                best_station = data_entity.link_stations[station]
                point = data_entity.points[point_index]
        return format(best_power, best_station, point)

def get_best_linkstation():
    result = dataprovider.get_data()
    power = get_best_station(result)
    return power