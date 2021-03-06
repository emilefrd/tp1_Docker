FROM python:3.8-buster

WORKDIR /tp1_

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .

EXPOSE 1000

CMD ["python3", "wrapper.py"]