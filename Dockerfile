FROM python:3.8-slim
COPY requirements.txt requirements.txt
RUN pip install --upgrade pip; apk add build-base; pip install numpy; pip install -r requirements.txt
RUN python -c "import numpy; print(numpy.__version__)"
COPY . /app
WORKDIR /app
ENTRYPOINT [ "python" ]
CMD ["app.py", "run", "--host=0.0.0.0"]
