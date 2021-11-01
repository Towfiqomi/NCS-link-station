import math
from apis.dtos import dtos
from apis.dataprovider import dataprovider


def get_euclidean_distance_for_point(point: dtos.Point, linkstation: dtos.LinkStation):
    """Receives point and linkstation data and retruns the distance between the
       given point and linkstation

    #Parameters:
        point:
            the data variable consists with the x and y coordinate of the points
        linkstations:
            the data variable consists with the x and y coordinate
            and the reach of the linkstation

    #Return:
        the euclidean distance between linkstations and points
    """
    return math.sqrt((point.x - linkstation.x) ** 2 + (point.y - linkstation.y) ** 2)


def get_power(linkstation: dtos.LinkStation, point: dtos.Point):
    """Receives point and linkstation data and retruns the power

    #Parameters:
        point:
            the data variable consists with the x and y coordinate of the points
        linkstations:
            the data variable consists with the x and y coordinate
            and the reach of the linkstation

    #Return:
        the power by calculating with the distance and linkstation reach
    """
    distance = get_euclidean_distance_for_point(point, linkstation)
    power = (linkstation.reach - distance) ** 2 if distance < linkstation.reach else 0
    return power


def format(power, best_station: dtos.LinkStation, point: dtos.Point):
    """Formats the result of best linkstation for given points

    #Parameters:
        power:
            the data variable contains the calculated power
        point:
            the data variable consists with the x and y coordinate of the points
        best_station:
            the data variable consists with the x and y coordinate
            and the reach of the linkstation

    #Return:
        the formatted string of end result
    """
    if power != 0:
        return "Best link station for point {}, {} is {}, {} with power {}".format(
            point.x, point.y, best_station.x, best_station.y, power
        )
    else:
        return "No link station within reach for point {}, {}".format(point.x, point.y)


def get_best_station(data_entity: dtos.DataEntity):
    """calculate the best link_station for the given point

    #Parameters:
        data_entity:
            the data variable contains the whole data object from the data.json file

    #Return:
        the formatted results of possible best stations for all given points
    """
    result = []
    point = dtos.Point
    best_station = dtos.LinkStation
    for point_index in range(len(data_entity.points)):
        for link_station_index in range(len(data_entity.link_stations)):
            best_power = 0
            power = get_power(
                data_entity.link_stations[link_station_index],
                data_entity.points[point_index],
            )
            if power > best_power:
                best_power = power
                best_station = data_entity.link_stations[link_station_index]
        point = data_entity.points[point_index]
        result.append(format(best_power, best_station, point))
    return result


def get_best_linkstation():
    """the model function that initiates the calculation of best linkstation
    #Return:
        the final results of best linkstations for all the given points
    """
    data = dataprovider.get_data()
    result = get_best_station(data)
    return result
