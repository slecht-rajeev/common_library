FROM python:3.10
WORKDIR /usr/src/app
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
RUN pip3 install --upgrade pip 
COPY ./requirements.txt /usr/src/app
RUN pip3 install -r requirements.txt
COPY . /usr/src/app
