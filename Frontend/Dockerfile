# FROM nginx:alpine

# COPY . /usr/share/nginx/html
# EXPOSE 80
# CMD ["nginx", "-g", "daemon off;"]

FROM registry.astralinux.ru/library/astra/ubi18-nodejs1819:latest


WORKDIR /app

# Копируем package.json и устанавливаем зависимости
RUN apt update && apt install -y nodejs npm
COPY package.json /app/
RUN npm install

# Копируем остальные файлы (index.html, index.js, main.css)
COPY . /app

EXPOSE 80

# Запускаем сервер для статических файлов на порту 80
CMD ["npm", "start"]