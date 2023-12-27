FROM python:3.9.18-slim
 
RUN pip install bs4 && pip install requests

COPY ./tvfinder-docker.py /app/tvfinder.py
ENTRYPOINT ["python3", "/app/tvfinder.py"]
CMD []
