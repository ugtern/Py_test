FROM python:3.7
ENV PYTHONUNBUFFERED 1
RUN mkdir /loop
WORKDIR /loop
ADD requirements.txt /loop/
RUN pip install -r requirements.txt
ADD . /loop/

CMD [ "python", "-u", "./loop/index.py" ]