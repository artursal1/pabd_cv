FROM python:3.8-slim-buster
LABEL authors="artursalmanov"

WORKDIR /ml-project
ADD . /ml-project
RUN pip3 install -r requirements.txt

CMD ["python3", "-m" , "flask", "run", "--host=0.0.0.0"]