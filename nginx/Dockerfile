# Use an official Nginx base image
FROM nginx:latest

COPY default.conf /etc/nginx/conf.d/

# Copy the current directory contents into the container at /usr/share/nginx/html
COPY . /usr/share/nginx/html
