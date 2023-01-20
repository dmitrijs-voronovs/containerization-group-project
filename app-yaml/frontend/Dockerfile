# Stage 1: Build an image that can build the Angular application
FROM node as build-container
# Specify the working directory inside the container
RUN mkdir -p /app/dist/out/
WORKDIR /app
# Copy the package*.json file inside the container so it can tell npm what packages to install
COPY package*.json /app/
# Run the installation of all the packages required in package*.json
RUN npm install
# Copy the source code of the application into the /app folder of the 
COPY . /app
# Specify that we want a production build (smaller)
ARG configuration=production
# Run the actual build and put the output in the folder /app/dist/out in the 
RUN npm run build
# Stage 2, create a container with nginx
# that serves the files created in the previous build
FROM nginx:latest
# We copy the files that were created in the previous build to the folder 
COPY  --from=build-container /app/build/ /usr/share/nginx/html
# We copy the nginx configuration frile form the host to the nginx 
COPY nginx.conf /etc/nginx/conf.d/default.conf
# Expose port
EXPOSE 80
# Start nginx
CMD ["nginx", "-g", "daemon off;"]

