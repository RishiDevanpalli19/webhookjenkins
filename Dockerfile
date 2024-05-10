FROM python:2.7
WORKDIR /app
COPY . /app
RUN pip install Flask
ENTRYPOINT ["python"]
CMD ["app.py"]
