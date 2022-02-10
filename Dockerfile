FROM docker.io/python:3.6-alpine
ENV PYTHONUNBUFFERED=0
USER root
COPY . /03143285
RUN chgrp -R 0 /03143285 \
    && chmod -R g=u /03143285
USER 1001
WORKDIR /03143285

ENTRYPOINT ["python"]
CMD ["-u", "app.py"]
