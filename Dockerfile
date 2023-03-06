FROM python:3.8.5-alpine

WORKDIR C:\\Users\\Manthan\\OneDrive\\Desktop\\Camera Website\\camerarental

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN pip install --upgrade pip
COPY ./requirements.txt /usr/src/app
RUN pip install -r requrements.txt

COPY . C:/Users/Manthan/OneDrive/Desktop/Camera Website/camerarental/

EXPOSE 8000

CMD ["python","manage.py","runserver","0.0.0.0.:8000"]
