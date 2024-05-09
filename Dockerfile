FROM python:3.8-slim

WORKDIR /app

COPY . /app

RUN pip install --no-cache-dir -r Requirements.txt

EXPOSE 5000

ENV FLASK_APP=application.py

# Run flask when the container launches
CMD ["flask", "run", "--host=0.0.0.0"]
