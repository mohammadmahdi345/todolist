FROM python:3.13.5

RUN apt-get update && apt-get install -y gcc libpq-dev

WORKDIR /app

COPY backend/r.txt ./

RUN pip install --upgrade pip && pip install -r r.txt

COPY backend/ /app/

EXPOSE 8000

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
