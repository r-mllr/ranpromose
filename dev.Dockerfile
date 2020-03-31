FROM python:3.8.2-alpine3.11

LABEL maintainer="Raphael Müller raphael.mueller@computational.bio.uni-giessen.de"

# Install Alpine Dependencies
RUN apk update && apk upgrade && apk add --update alpine-sdk && \
    apk add --no-cache bash git openssh make cmake 

RUN mkdir -p /app
COPY requirements.txt /app
WORKDIR /app

RUN pip install -r requirements.txt

COPY . /app

ENTRYPOINT ["make"]

CMD ["run"]
