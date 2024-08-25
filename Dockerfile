FROM python:3.12-slim

RUN apt update
RUN apt install -y default-jre
RUN apt install -y poppler-utils
RUN apt clean

WORKDIR /app

COPY requirements.txt /app/

RUN pip install --no-cache-dir -r requirements.txt

COPY . /app/

CMD ["python", "extract.py"]