FROM node:16.19.0-alpine3.17 as build-container

WORKDIR /app

COPY package*.json /app/

RUN npm install

COPY . /app

RUN npm run build -- --outputPath=./dist/out

