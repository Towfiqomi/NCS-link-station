from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

from apis import config, routes


def application_details() -> FastAPI:
    application = FastAPI(
        title=config.API_NAME,
        description=config.API_DESCRIPTION,
        version=config.API_VERSION,
    )
    application.include_router(routes.router, prefix=config.API_ROUTE_PREFIX)
    application.add_middleware(
        CORSMiddleware,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )
    return application


app = application_details()
