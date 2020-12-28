FROM python:3
USER root
RUN mkdir /Food.proj
RUN chmod -R 755 /Food.proj
COPY *.py /Food.proj/
COPY configurations.json /Food.proj/
WORKDIR "/Food.proj"
ENTRYPOINT ["/usr/local/bin/python3", "//main.py"]