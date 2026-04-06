FROM python:3.12-alpine3.19

USER "1000:1000"

EXPOSE 8080

HEALTHCHECK CMD curl -f http://localhost/ || exit 1

WORKDIR /app

ENV SERVER_HOST=""

ENV SERVER_PORT=8080

COPY app.py .

CMD ["python", "app.py"]