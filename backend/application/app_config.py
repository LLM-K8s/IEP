from pathlib import Path
from typing import List

from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse
from fastapi.routing import APIRouter

from infrastructure.config import settings


class AppConfig:
    def __init__(self, app: FastAPI, frontend_dist_dir: Path):
        self.app = app
        self.frontend_dist_dir = frontend_dist_dir
        self._setup_cors()
        self._setup_middleware()

    def _setup_cors(self) -> None:
        origins: List[str] = [*settings.CORS_ORIGINS]
        self.app.add_middleware(
            CORSMiddleware,
            allow_origins=origins,
            allow_credentials=True,
            allow_methods=['*'],
            allow_headers=['*'],
        )

    def _setup_middleware(self) -> None:
        @self.app.middleware('http')
        async def spa_handler(request: Request, call_next):
            path = request.url.path

            # 排除 API 與 FastAPI 自身路由
            excluded_prefixes = ('/api', '/docs', '/redoc', '/openapi.json')
            if path.startswith(excluded_prefixes):
                return await call_next(request)

            # 若是靜態檔案存在 => 回傳檔案
            full_path = self.frontend_dist_dir / path.lstrip('/')
            if full_path.is_file():
                return FileResponse(full_path)

            # 其他全部 fallback 到 index.html（給 SPA）
            return FileResponse(self.frontend_dist_dir / 'index.html')

    def include_routers(self, routers: List[APIRouter]) -> None:
        for router in routers:
            self.app.include_router(router, prefix='/api')
