from fastapi import FastAPI
from app.routers.routes_defined_with_api import router
from app.database import Base,engine
app = FastAPI()

app.include_router(router)

Base.metadata.create_all(engine)

