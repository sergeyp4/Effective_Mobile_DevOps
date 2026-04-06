FROM python:3.12-alpine3.19

WORKDIR /app

COPY app.py .

EXPOSE 8080

HEALTHCHECK CMD curl -f http://localhost/ || exit 1

CMD ["python", "app.py"]