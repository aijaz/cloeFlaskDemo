FROM python:3.12

WORKDIR /
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
RUN mkdir app
COPY . app
CMD ["gunicorn", "-w 4", "-b 0.0.0.0:8000", "app.flask_app:my_flask_app"]
EXPOSE 8000
