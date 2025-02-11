from fastapi import FastAPI

from src.api.router import all_routers


app = FastAPI(title="Books and Authors")

for router in all_routers:
    app.include_router(router)
