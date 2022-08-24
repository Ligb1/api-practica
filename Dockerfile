FROM python:3.9
WORKDIR /code
COPY ./requirements.txt /code/requirements.txt 
COPY ./pruebafb.json /code/pruebafb.json
RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt
EXPOSE 8090
COPY ./app /code/app
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8090"]
