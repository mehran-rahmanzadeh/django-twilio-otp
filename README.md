# Django twilio OTP
### Stack
- Python 3.8
- Django 3.2
- PostgreSQL

### Description
This is a Django app that allows you to send OTPs to your users over SMS and voice.

### Running
- Copy sample config
```bash
cp docs/docker/settings.ini .
```
- Build
```bash
docker compose up -d --build
# or in older version: docker-compose up -d
```
- Run tests
```bash
docker exec -it otp_django python manage.py test
```
Possible issues:
- if database does not exist error occurs, try to create `otp` database in `otp_postgres` container
- if you can not log in to admin panel, try to create superuser in `otp_django` container

### Usage
You can use provided API endpoints:
- `/api/v1/send-token/`
- `/api/v1/verify-token/`