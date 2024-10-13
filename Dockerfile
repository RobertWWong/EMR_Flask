FROM python:3.10.12

WORKDIR /usr/src/app

COPY requirements.txt ./
RUN pip install --upgrade pip

RUN pip install --no-cache-dir -r requirements.txt

COPY . .
#CMD [ "Echo","ls" ]
CMD [ "python", "main.py" ]
#RUN flask --app main run