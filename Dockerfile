FROM python:3.11-slim

ENV PYTHONUNBUFFERED=1
ENV POETRY_VIRTUALENVS_CREATE=false
ENV POETRY_NO_INTERACTION=1

# system deps
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    curl \
    git \
    && rm -rf /var/lib/apt/lists/*

# install poetry
RUN pip install --no-cache-dir poetry==1.6.1

WORKDIR /app

# copy poetry files first for caching
COPY pyproject.toml poetry.lock* /app/

RUN poetry install --no-dev --no-root

# copy app
COPY . /app

EXPOSE 8000

CMD ["uvicorn", "braumchat_api.main:app", "--host", "0.0.0.0", "--port", "8000"]
