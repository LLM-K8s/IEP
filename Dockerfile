FROM alpine:3.21.2

WORKDIR /app

ENV PYTHONUNBUFFERED=1
ENV PATH="/root/.local/bin:$PATH"

RUN apk update && apk upgrade \
    && apk add --no-cache nodejs python3 py3-pip npm wget curl nano git openssh gnupg \
    && ln -sf python3 /usr/bin/python \
    && curl -sSL https://install.python-poetry.org | python3 - \
    && poetry config virtualenvs.in-project true

EXPOSE 5173

CMD ["/bin/sh"]