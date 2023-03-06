FROM python:3.8.5-alpine

WORKDIR C:\\Users\\Manthan\\OneDrive\\Desktop\\camerarental\\camerarental

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN pip install --upgrade pip
COPY ./requirements.txt C:/Users/Manthan/OneDrive/Desktop/camerarental/camerarental/
RUN pip install -r requirements.txt

COPY . C:/Users/Manthan/OneDrive/Desktop/camerarental/camerarental/

EXPOSE 8000

CMD ["python","manage.py","runserver","0.0.0.0.:8000"]
