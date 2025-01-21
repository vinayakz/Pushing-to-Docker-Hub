# base image
FROM python:3.11


# Working directory
WORKDIR /app

# code
COPY . .

# required liberies
RUN pip install -r requirements.txt


# run
CMD ["python", "run.py"]
