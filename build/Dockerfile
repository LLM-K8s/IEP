########################################
# Frontend Builder Stage
########################################
FROM node:22-alpine AS frontend-builder

LABEL stage="builder"

WORKDIR /app

COPY frontend/package*.json ./
RUN npm ci

COPY frontend/ ./
RUN npm run build



########################################
# Backend Builder Stage
########################################
FROM python:3.11-slim AS backend-builder

WORKDIR /app

# 安裝構建依賴
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential=12.9ubuntu3 \
    && rm -rf /var/lib/apt/lists/*

# 複製依賴文件
COPY backend/pyproject.toml backend/uv.lock ./

# 安裝 uv
RUN pip install uv

# 使用 uv 安裝依賴
RUN uv pip install --system -e .

########################################
# Runtime Stage
########################################
FROM python:3.11-slim

WORKDIR /app

# 複製構建階段的依賴
COPY --from=backend-builder /usr/local/lib/python3.11/site-packages /usr/local/lib/python3.11/site-packages
COPY --from=frontend-builder /app/dist /app/dist

# 複製應用程式代碼
COPY backend /app

# 設置環境變數
ENV PYTHONPATH=/app
ENV PYTHONUNBUFFERED=1
ENV FRONTEND_DIST_DIR=/app/dist

# 暴露端口
EXPOSE 8000

# 啟動應用
CMD ["python", "main.py"]