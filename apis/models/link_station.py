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
    result =  math.sqrt(abs((point.x - linkstation.x) ** 2) + (abs(point.y - linkstation.y) ** 2))
    return result


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
    power = math.pow((linkstation.reach - distance),2) if distance < linkstation.reach else 0
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
    if power:
        return "Best link station for point {}, {} is {}, {} with power {}".format(
            point.x, point.y, best_station.x, best_station.y, power
        )
    else:
        return "No link station within reach for point {}, {}".format(point.x, point.y)


def get_best_station(point: dtos.Point, link_stations: list[dtos.LinkStation]):
    """calculate the best link_station for the given point

    #Parameters:
        data_entity:
            the data variable contains the whole data object from the data.json file

    #Return:
        the formatted results of possible best stations for all given points
    """
    best_power = 0
    best_station = link_stations[0]
    for link_station in link_stations:
        power = get_power(
                link_station,
                point,
        )
        if power > best_power:
            best_power = power
            best_station = link_station
        result = format(best_power, best_station, point)
    return result


def get_best_linkstation():
    """the model function that initiates the calculation of best linkstation
    #Return:
        the final results of best linkstations for all the given points
    """
    data = dataprovider.get_data()
    result = []
    for point in data.points:
        result.append(get_best_station(point, data.link_stations))
    return result
