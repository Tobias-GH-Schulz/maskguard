FROM python:3.8.0

# remember to expose the port your app'll be exposed on.
EXPOSE 80

RUN apt-get update
RUN apt-get install ffmpeg libsm6 libxext6  -y

RUN pip install -U pip

COPY requirements.txt app/requirements.txt
RUN pip install --no-cache-dir -r app/requirements.txt
# copy into a directory of its own (so it isn't in the toplevel dir)
COPY . /app
WORKDIR /app

# run it!
ENTRYPOINT ["streamlit", "run", "app.py", "--server.port=80", "--server.address=0.0.0.0", "--server.maxUploadSize=20"]
