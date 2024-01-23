FROM python:3.9

WORKDIR /zoomcamp24
COPY ./ /zoomcamp24

ENV PYTHONPATH=${PYTHONPATH}:${PWD}
ENV SOME_OTHER_ENV_VARIABLE=X

RUN mkdir -p .docker_volumes/downloads

RUN pip3 install --upgrade pip
RUN pip3 install poetry
RUN poetry config virtualenvs.create false
RUN poetry install --no-dev

# ENTRYPOINT ["python","src/app/data/etl/main.py"]
ENTRYPOINT ["bash"]
