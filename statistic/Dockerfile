FROM tiangolo/uvicorn-gunicorn-fastapi:python3.9

WORKDIR /statistic

COPY ./statistic /statistic

COPY ./commom /statistic/commom

RUN pip install -r /statistic/requirements.txt


