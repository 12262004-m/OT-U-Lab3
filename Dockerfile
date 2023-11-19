FROM python:3.11.5

RUN apt-get update && apt-get clean

ADD file.py .
ADD test.py .

RUN ["python3", "./test.py"]
RUN echo "Test completed!" >> result.txt