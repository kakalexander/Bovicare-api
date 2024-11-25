# bovicare-api/Dockerfile
FROM python:3.11.0-slim

WORKDIR /app

# Instalar dependências necessárias para compilar o psycopg2
RUN apt-get update && \
    apt-get install -y \
    libpq-dev \
    build-essential && \
    rm -rf /var/lib/apt/lists/*

# Copiar o requirements.txt para instalar as dependências do Python
COPY requirements.txt /app/requirements.txt

# Instalar pacotes Python
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

COPY . .

EXPOSE 4000

CMD ["flask", "run", "--host=0.0.0.0", "--port=4000"]
