FROM ubuntu:latest
 
RUN apt-get update && apt-get install -y --no-install-recommends python3 python3-pip && \
rm -rf /var/lib/apt/lists/* && \
pip install bs4 && \
pip install requests

COPY ./tvfinder-docker.py /app/tvfinder.py
ENTRYPOINT ["python3", "/app/tvfinder.py"]
CMD ["param1", "param2"]
