from typing import Dict, List
from pydantic import BaseModel


class LinkStation(BaseModel):
    x: int
    y: int
    reach : int

class Point(BaseModel):
    x: int
    y: int

class DataEntity(BaseModel):
    link_stations : List[LinkStation]
    points : List[Point]