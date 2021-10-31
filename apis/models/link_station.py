import json
from apis.dataprovider import dataprovider

def get_best_linkstation():
    linkstation, device = dataprovider.get_data()
    return linkstation, device