### Комментарий к вашему ТЗ от проверяющего.###
**Плюсы:**
1) Используются alpine образы (python:3.12-alpine3.19, nginxinc/nginx-unprivileged:1.29-alpine-slim)
2) Приложение запускается от непривилегированного пользователя (UID 1000:1000 в обоих контейнерах)
3) Backend порт 8080 НЕ публикуется наружу (только внутренняя docker-сеть)
4) Nginx передаёт заголовки (Host, X-Real-IP, X-Forwarded-For)
5) Кастомная docker-сеть (app-network) определена
6) HEALTHCHECK настроен для backend с интервалом 3s
7) restart: unless-stopped для обоих сервисов
8) Безопасность: cap_drop: ALL и no-new-privileges:true
9) depends_on корректно настроен
10) Понятная структура проекта: backend/, nginx/
11) README с описанием схемы прохождения трафика и особенностей реализации
12) Кастомный healthcheck бинарник (httpcheck) вместо curl
13) Логичные коммиты без ИИ-стилистики
14) Обработка 404 в backend (необязательно, но хорошо)
 
**Что можно улучшить:**
1) .gitignore содержит только имя PDF файла (отсутствует .env, Dockerfile и т.д.)
2) Нет .dockerignore
3) Нет upstream блока в nginx.conf
4) В nginx.conf отсутствует заголовок X-Forwarded-Proto
5) USER 1000:1000 в backend Dockerfile указан до WORKDIR (может вызвать проблемы с правами при создании директории)
6) Нет healthcheck для nginx
7) В docker-compose.yml сервисы не подключены к сети app-network (сеть определена, но не используется)
8) Отсутствует troubleshooting раздел в README
