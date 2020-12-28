FROM python:3
USER root
RUN mkdir /foodproj
RUN chmod -R 755 /foodproj
COPY *.py /foodproj/
COPY configurations.json /foodproj/
WORKDIR "/foodproj"
ENTRYPOINT ["/usr/local/bin/python3", "/foodproj/main.py"]
