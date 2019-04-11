FROM python:2.7-slim

RUN pip install --upgrade pip

WORKDIR /app

COPY . /app

RUN pip --no-cache-dir install -r requirements.txt                                                                            

EXPOSE 5000

ENTRYPOINT  ["python"]

CMD ["web-service.py"]