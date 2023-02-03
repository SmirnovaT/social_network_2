FROM python:3.10

# Set environment varibles
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /code/

RUN pip install poetry


COPY poetry.lock pyproject.toml /code/
RUN poetry config virtualenvs.create false
RUN python -m poetry install

COPY . /code/
#RUN poetry config virtualenvs.create false && poetry install && rm -rf /code/
EXPOSE 8000