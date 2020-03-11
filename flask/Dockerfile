#use python container image
FROM python:3.6.9-stretch

#set the working directory
WORKDIR /app

#copy the current directory
ADD . /app

#install dependencies
RUN pip install -r requirements.txt

CMD ["gunicorn", "app.ini"]