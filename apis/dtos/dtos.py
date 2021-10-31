from typing import Dict
from pydantic import BaseModel


class LinkStation(BaseModel):
    x: int
    y: int
    reach : int