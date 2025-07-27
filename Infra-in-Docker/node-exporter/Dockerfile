FROM ubuntu:latest
RUN apt-get update && apt-get install -y wget tar
WORKDIR /opt
RUN wget https://github.com/prometheus/node_exporter/releases/download/v1.8.1/node_exporter-1.8.1.linux-amd64.tar.gz \
    && tar xvf node_exporter-1.8.1.linux-amd64.tar.gz \
    && mv node_exporter-1.8.1.linux-amd64 node_exporter \
    && rm node_exporter-1.8.1.linux-amd64.tar.gz
EXPOSE 9100
CMD ["/opt/node_exporter/node_exporter"]