FROM ubuntu:22.04

RUN apt-get update && \
    apt-get install -y \
    fortune-mod \
    cowsay \
    netcat-openbsd \
    bash && \
    rm -rf /var/lib/apt/lists/*

ENV PATH="/usr/games:${PATH}"

WORKDIR /app

COPY . .

RUN sed -i 's/\r$//' wisecow.sh && \
    chmod +x wisecow.sh

EXPOSE 4499

CMD ["./wisecow.sh"]