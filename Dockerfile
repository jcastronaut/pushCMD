FROM python:3

COPY ./ ./


CMD python test.py 1 2 3 4 


CMD tail -f /dev/null

