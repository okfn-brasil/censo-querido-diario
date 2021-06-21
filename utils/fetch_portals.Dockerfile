FROM python:3.8.5-slim

# Setup env
ENV LANG C.UTF-8
ENV LC_ALL C.UTF-8
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONFAULTHANDLER 1

RUN mkdir /usr/src/app
WORKDIR /usr/src/app

COPY . .

RUN python -m pip install .

# Run the executable
ENTRYPOINT ["fetch-portals"]
