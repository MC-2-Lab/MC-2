FROM nginx:latest
ENV PYTHONUNBUFFERED 1
ENV NVIDIA_VISIBLE_DEVICES ALL
ADD . /tmp
RUN sh /tmp/build.sh
RUN pip install -r /tmp/requirements.txt
RUN mkdir /src
WORKDIR /src
