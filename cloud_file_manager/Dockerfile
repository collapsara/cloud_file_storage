FROM python:3.9.1

WORKDIR /home/cloud_file_manager/

RUN pip install --upgrade pip

COPY cloud_file_manager/requirements.txt /home/cloud_file_manager/requirements.txt
RUN pip install -r requirements.txt

COPY cloud_file_manager/ /home/cloud_file_manager/