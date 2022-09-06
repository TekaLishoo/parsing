FROM python:3.10 as base

ENV PYTHONUNBUFFERED=1

RUN pip install pipenv

WORKDIR /app

COPY . /app/

RUN pipenv install --system --deploy

CMD ["uvicorn", "main:app", "--reload", "--host", "0.0.0.0"]