from fastapi import APIRouter
from apis.models import link_station

router = APIRouter()


@router.get("/link-station")
def get_best_linkstation():
    result = link_station.get_best_linkstation()
    return result
