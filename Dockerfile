FROM python:3.10-slim

WORKDIR /app

COPY app.py calci.sh /app

RUN chmod +x calci.sh
RUN pip install flask

CMD ["python","app.py"]

