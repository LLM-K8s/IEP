from typing import List

from pydantic import Field
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    """應用程式配置設定"""

    # 應用程式基本設定
    APP_NAME: str = 'IEP Backend'
    DEBUG: bool = Field(default=False, env='DEBUG')
    API_V1_PREFIX: str = '/api'

    # 資料庫設定
    MONGODB_URL: str = Field(default='mongodb://172.16.3.49:27017', env='MONGODB_URL')
    MONGODB_DB_NAME: str = Field(default='testDB', env='MONGODB_DB_NAME')

    # 其他設定
    CORS_ORIGINS: List[str] = Field(default=['*'], env='CORS_ORIGINS')

    # 認證設定
    OIDC_ISSUER: str = Field(default='http://172.16.1.16:8081/realms/coder', env='OIDC_ISSUER')
    OIDC_AUDIENCE: str = Field(default='account', env='OIDC_AUDIENCE')

    # Minio設定
    MINIO_ENDPOINT: str = Field(default='172.16.3.49:9000', env='MINIO_ENDPOINT')
    MINIO_ACCESS_KEY: str = Field(default='minioadmin', env='MINIO_ACCESS_KEY')
    MINIO_SECRET_KEY: str = Field(default='minioadmin', env='MINIO_SECRET_KEY')
    MINIO_BUCKET: str = Field(default='coursefile', env='MINIO_BUCKET')


# 創建全局配置實例
settings = Settings()
