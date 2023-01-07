FROM python:3.11.1-alpine

WORKDIR /app

COPY ./requirements.txt /app/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /app/requirements.txt

COPY ./ /app

WORKDIR /app/codeAlong

CMD ["./manage.py runserver"]
