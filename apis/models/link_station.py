import json
from apis.dataprovider import dataprovider



def get_best_linkstation():
    result = dataprovider.get_data()
    return result