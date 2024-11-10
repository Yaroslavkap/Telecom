FROM registry.astralinux.ru/library/astra/ubi18-nodejs1819:latest


WORKDIR /app


RUN apt update && apt install -y nodejs npm
COPY package.json /app/
RUN npm install

COPY . /app

EXPOSE 80

CMD ["npm", "start"]