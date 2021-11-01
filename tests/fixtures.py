
import pytest
from apis.dtos import dtos

def data_entity() -> dtos.DataEntity:
    return {
        "link_stations": [
            {
                "x": 0,
                "y": 0,
                "reach": 12,
            },
            {
                "x": 100,
                "y": 100,
                "reach": 20,
            },
        ],
        "points": [
            {
                "x": 10,
                "y": 12,
            },
            {
                "x": 20,
                "y": 30,
            },
        ]
    }