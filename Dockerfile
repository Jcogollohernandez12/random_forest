FROM tiangolo/uwsgi-nginx-flask:python3.6
WORKDIR /app
ENV FLASK_APP=app.py
ENV FLASK_RUN_HOST=0.0.0.0
ENV ENVIRONMENT=development
COPY requirements.txt /app
RUN pip install -r ./requirements.txt
EXPOSE 5000
COPY . .
CMD ["flask","run"]