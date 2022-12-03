FROM python:3.8

#for optimization container 1 -> True
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

#workdir is project Root derictory
WORKDIR /DevKg

#copy dependencies in workdir
COPY requirements.txt /DEVKG/

#install dependencies
# RUN pip3 install -r requirements.txt 
RUN pip3 install --upgrade pip

RUN pip3 freeze > requirements.txt 

#copy our project to workdir
COPY . /DevKg

EXPOSE 8000

CMD ["python3" ,"manage.py" ,"runserver" ,"0.0.0.0:8000"]