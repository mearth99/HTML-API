FROM python:3.10.4

RUN pip3 install flask requests

WORKDIR /usr/src/app

CMD ["python3", "app.py"]