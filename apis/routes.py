from fastapi import APIRouter
from apis.views import link_station

router = APIRouter()

router.include_router(link_station.router, tags=["Link Station"])
