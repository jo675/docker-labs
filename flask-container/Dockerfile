FROM python:alpine

WORKDIR /home/

COPY . .

RUN pip install flask

EXPOSE 81

ENTRYPOINT ["python"]

CMD ["app.py"]