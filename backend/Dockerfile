FROM python:3.9.5
ADD . /extensionWorker
WORKDIR /extensionWorker
RUN pip3 install -r requirements.txt
ENV FLASK_APP=app.py
ENV FLASK_RUN_HOST=0.0.0.0
EXPOSE 5000
CMD ["flask", "run"]
