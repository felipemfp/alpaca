FROM python:3-alpine
LABEL maintainer="felipemfpontes@gmail.com"

ENV FLASK_APP alpaca.py

WORKDIR /usr/src/app

COPY . /usr/src/app

RUN pip install --no-cache-dir pipenv

RUN pipenv install --system --deploy

EXPOSE 5000

CMD ["flask", "run", "--host=0.0.0.0"]