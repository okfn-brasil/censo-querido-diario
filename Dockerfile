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

RUN python censo/manage.py collectstatic --no-input

CMD ["gunicorn", "censo.wsgi:application", "--reload", "--bind", "0.0.0.0:1337"]
CMD ["python", "censo/manage.py", "runserver", "0.0.0.0:8000"]