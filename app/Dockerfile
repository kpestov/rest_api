FROM python:3.6

EXPOSE 5000

WORKDIR /app

COPY . /app

CMD virtualenv -p python3 venv
RUN pip install -r requirements.txt

CMD python main.py