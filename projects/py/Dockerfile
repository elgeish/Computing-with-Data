FROM python:3

COPY . .
RUN apt-get -qq update && apt-get -qq install -y libhdf5-serial-dev
RUN pip install --no-cache-dir -r requirements.txt
