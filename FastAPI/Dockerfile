FROM python:3.9
RUN apt-get update && apt-get install -y libgomp1
COPY requirement.txt .
RUN pip install -r requirement.txt
COPY . /app
WORKDIR /app
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "5000"]
