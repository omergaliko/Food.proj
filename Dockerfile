FROM python:3
USER root
RUN mkdir /FoodProj
RUN chmod -R 755 /FoodProj
COPY *.py /Food.proj/
COPY configurations.json /FoodProj/
WORKDIR "/FoodProj"
ENTRYPOINT ["/usr/local/bin/python3", "/FoodProj/main.py"]
