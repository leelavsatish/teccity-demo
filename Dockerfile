FROM python:3.10-slim

# Install dependencies
RUN apt-get update && apt-get install -y nginx supervisor && rm -rf /var/lib/apt/lists/*

# Set workdir
WORKDIR /app

# Copy backend
COPY backend/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY backend/ .

# Copy frontend
COPY frontend/ /usr/share/nginx/html

# Copy configs
COPY nginx.conf /etc/nginx/nginx.conf
COPY supervisord.conf /etc/supervisor/conf.d/supervisord.conf

# Expose ports
EXPOSE 80

# Start both services
CMD ["supervisord", "-c", "/etc/supervisor/conf.d/supervisord.conf"]
