FROM python:3.7-slim
ENV PYTHONUNBUFFERED 1
ENV IN_DOCKER 1
RUN mkdir /code
WORKDIR /code
COPY requirements.txt /code/
RUN pip install -r requirements.txt
COPY . /code/
ENTRYPOINT [ "bash", "entrypoint.sh" ]
