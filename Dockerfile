# Stage 1: Build backend
FROM python:3.10-slim AS backend
WORKDIR /app
COPY backend/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY backend/ .

# Stage 2: Build frontend
FROM nginx:alpine AS frontend
WORKDIR /usr/share/nginx/html
COPY frontend/ .

# Stage 3: Final combined image
FROM python:3.10-slim
WORKDIR /app

# Copy backend from backend stage
COPY --from=backend /app /app

# Install nginx + supervisor
RUN apt-get update && apt-get install -y nginx supervisor && rm -rf /var/lib/apt/lists/*

# Copy frontend from frontend stage
COPY --from=frontend /usr/share/nginx/html /usr/share/nginx/html

# Configure nginx
COPY nginx.conf /etc/nginx/nginx.conf

# Copy supervisor config
COPY supervisord.conf /etc/supervisor/conf.d/supervisord.conf

EXPOSE 5000 80

CMD ["supervisord", "-c", "/etc/supervisor/conf.d/supervisord.conf"]
