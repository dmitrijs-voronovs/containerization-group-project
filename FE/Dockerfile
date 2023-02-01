FROM node:18
WORKDIR /app
COPY package*.json ./
RUN npm install
COPY . .

RUN npm run build 
ENV PORT 5050
EXPOSE 5050

CMD ["npm", "run", "start"]