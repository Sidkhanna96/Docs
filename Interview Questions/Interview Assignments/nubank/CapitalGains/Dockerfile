FROM python:3.11-slim

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

USER root

WORKDIR /app

# minimal system deps for building wheels if needed
RUN apt-get update && apt-get install -y --no-install-recommends build-essential \
    && rm -rf /var/lib/apt/lists/*

# copy dependency metadata
COPY pyproject.toml poetry.lock* /app/

# upgrade pip and install the package
RUN pip install --upgrade pip setuptools wheel \
    && pip install .

# copy source
COPY . /app

# default entry: run the CLI (reads stdin)
ENTRYPOINT ["python", "main.py"]