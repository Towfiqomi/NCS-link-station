import math
from apis.dtos import dtos
from apis.dataprovider import dataprovider

def get_euclidean_distance_for_point(point : dtos.Point, linkstation:dtos.LinkStation):
    return math.sqrt((point.x-linkstation.x)**2 + (point.y-linkstation.y)**2)

def get_power(linkstation : dtos.LinkStation, point : dtos.Point):
    distance = get_euclidean_distance_for_point(point, linkstation)
    power = (linkstation.reach - distance)**2 if distance < linkstation.reach else 0
    return power

def format(power, best_station : dtos.LinkStation, point : dtos.Point):
    if power != 0:
        return "Best link station for point {}, {} is {}, {} with power {}".format(point.x, point.y, best_station.x, best_station.y, power)
    else:
        return "No link station within reach for point {}, {}".format(point.x, point.y)

def get_best_station(data_entity : dtos.DataEntity):
    result = []
    point = dtos.Point
    best_station = dtos.LinkStation
    for point_index in range(len(data_entity.points)):
        for link_station_index in range(len(data_entity.link_stations)):
            best_power = 0
            power = get_power(data_entity.link_stations[link_station_index], data_entity.points[point_index])
            if power > best_power:
                best_power = power
                best_station = data_entity.link_stations[link_station_index]
        point = data_entity.points[point_index]
        result.append(format(best_power, best_station, point))
    return result

def get_best_linkstation():
    data = dataprovider.get_data()
    power = get_best_station(data)
    return power