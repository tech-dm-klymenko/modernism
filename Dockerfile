FROM python:3.11  AS builder

WORKDIR /usr/src/app

RUN apt-get update

COPY requirements.txt .

RUN python -m venv /venv && \
    /venv/bin/pip install --upgrade pip && \
    /venv/bin/pip install -r requirements.txt


RUN python -m venv /venv && \
    /venv/bin/pip install --upgrade pip && \
    /venv/bin/pip install -r requirements.txt

FROM python:3.11-slim-buster

WORKDIR /usr/src/app

COPY --from=builder /venv /venv

COPY . .

RUN chmod +x entrypoint.sh

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV PATH="/venv/bin:$PATH"

ENTRYPOINT ["./entrypoint.sh"]

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]