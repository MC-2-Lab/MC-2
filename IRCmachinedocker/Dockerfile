FROM nvidia/cuda:11.3.0-base-ubuntu20.04
ENV PYTHONUNBUFFERED 1
ENV NVIDIA_VISIBLE_DEVICES ALL
ADD . /tmp
# RUN pip install -r /tmp/requirements.txt
# RUN sh /tmp/build.sh
RUN mkdir /src
WORKDIR /src
