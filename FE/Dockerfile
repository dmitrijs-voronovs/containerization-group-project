FROM node:18-alpine
WORKDIR /app
COPY package*.json ./
RUN npm install
COPY . .

ARG API_SERVICE_SERVICE_HOST
ARG API_SERVICE_SERVICE_PORT
ENV API_SERVICE_SERVICE_HOST=${API_SERVICE_SERVICE_HOST}
ENV API_SERVICE_SERVICE_PORT=${API_SERVICE_SERVICE_PORT}

RUN npm run build 
ENV PORT 5050
EXPOSE 5050

# CMD ["npm", "run", "build", "&&", "npm", "run", "start"]
# CMD ["npm", "run", "dev"]
CMD ["npm", "run", "start"]
# CMD ["npm", "run", "prod"]