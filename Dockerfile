FROM python:3.7.2-alpine

ENV PYTHONBREAKPOINT=ipdb.set_trace
ENV SECRET_KEY=temporary-secret-key-to-generate-staticfiles

RUN mkdir /code
WORKDIR /code

COPY requirements.txt /code/
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

COPY . .

RUN python manage.py collectstatic --no-input

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]