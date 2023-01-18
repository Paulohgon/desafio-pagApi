from fastapi import FastAPI

from entrypoints.receiver import router as receiver_router
from entrypoints.databasedump import router as database_router
from entrypoints.pix import router as pix_router

class routingMap:
    @staticmethod
    def create(app:FastAPI):

        @app.get("/ping", status_code=200, description="Liveliness Check")
        async def ping():
            return {"ping": "pong"}

        app.include_router(receiver_router,
            prefix="/receiver",
            tags=["receiver"]
        )
        app.include_router(database_router,
            prefix="/database",
            tags=["database"]
        )
        app.include_router(pix_router,
            prefix="/pix",
            tags=["pix"]
        )
        