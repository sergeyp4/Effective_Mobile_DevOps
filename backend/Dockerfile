FROM python:3.12-alpine3.19

USER "1000:1000"

EXPOSE 8080

WORKDIR /app

COPY app.py .

COPY --from=ghcr.io/tarampampam/microcheck:1 /bin/httpcheck /bin/httpcheck

HEALTHCHECK --interval=3s --timeout=1s CMD ["httpcheck", "http://localhost:8080/"]

CMD ["python", "app.py"]