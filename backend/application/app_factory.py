from contextlib import asynccontextmanager
from pathlib import Path
from typing import List

from fastapi import FastAPI
from fastapi.routing import APIRouter

from application.app_config import AppConfig
from infrastructure.mongodb import close_mongodb, init_mongodb


class AppFactory:
    def __init__(self, frontend_dist_dir: Path):
        self.frontend_dist_dir = frontend_dist_dir

    @asynccontextmanager
    async def _lifespan(self, app: FastAPI):
        await init_mongodb(app)
        yield
        await close_mongodb(app)

    def create_app(self, routers: List[APIRouter]) -> FastAPI:
        app = FastAPI(lifespan=self._lifespan)
        app_config = AppConfig(app, self.frontend_dist_dir)
        app_config.include_routers(routers)
        return app
