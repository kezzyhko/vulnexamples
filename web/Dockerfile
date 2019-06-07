FROM python:3.6.4
RUN mkdir /web
WORKDIR /web
COPY . /web/
RUN pip3 install -r requirements.txt
RUN python3 manage.py collectstatic --no-input
RUN python3 manage.py makemigrations