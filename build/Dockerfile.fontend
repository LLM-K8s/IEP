########################################
# Builder Stage
########################################
FROM node:22-alpine AS builder

LABEL stage="builder"

WORKDIR /app

COPY frontend/package*.json ./
RUN npm ci

COPY frontend/ ./
RUN npm run build


########################################
# Production Stage
########################################
FROM nginx:alpine

ARG BUILD_DATE
ARG VERSION

LABEL version="${VERSION}"
LABEL build_date="${BUILD_DATE}"

# Set nginx user permissions
RUN chown -R nginx:nginx /var/cache/nginx && \
    chown -R nginx:nginx /var/log/nginx && \
    chown -R nginx:nginx /etc/nginx/conf.d && \
    touch /var/run/nginx.pid && \
    chown -R nginx:nginx /var/run/nginx.pid


WORKDIR /usr/share/nginx/html

COPY --from=builder /app/dist ./
COPY build/nginx.conf /etc/nginx/conf.d/default.conf

# Set appropriate permissions
RUN chown -R nginx:nginx /usr/share/nginx/html

# Switch to non-root user
USER nginx


EXPOSE 80

CMD ["nginx", "-g", "daemon off;"]