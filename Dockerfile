FROM python:3

COPY ./ ./

ENTRYPOINT /run.sh
