FROM python:3.11-alpine

RUN mkdir /app
WORKDIR /app
COPY . .
RUN --mount=type=cache,id=custom-pip,target=/root/.cache/pip pip install -r req.txt
