FROM python:3.7
ENV PYTHONUNBUFFERED 1
RUN mkdir /web_app
WORKDIR /web_app
ADD requirements.txt /web_app/
RUN pip install -r requirements.txt
ADD . /web_app/

CMD [ "python", "-u", "./web_app/index.py" ]