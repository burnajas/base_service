FROM python:3.7

#RUN apt-get update -y
#RUN apt-get install python3-dev default-libmysqlclient-dev build-essential -y
#RUN apt-get install postgresql -y

# Docker arguments and defaults (default to `test` environment)
ARG ENVIRONMENT_TYPE
ARG DATABASE_USERNAME
ARG DATABASE_PASSWORD
ARG DATABASE_URL='db'
ARG DATABASE='app_db'

# Environment variables
ENV ENVIRONMENT_TYPE=$ENVIRONMENT_TYPE
ENV DATABASE_USERNAME=$DATABASE_USERNAME
ENV DATABASE_PASSWORD=$DATABASE_PASSWORD
ENV DATABASE_URL=$DATABASE_URL
ENV DATABASE=$DATABASE

# Create a directory for the project code
RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app

# Copy code from host into container
COPY ./code /usr/src/app

# Install packages
#RUN pip3 install --no-cache-dir -r requirements.txt
RUN pip install --no-index --find-links=whl/ -r requirements.txt

# Add MySQL Client
#RUN mkdir -p /usr/src/app/dependencies
#ADD ./code/dependencies /usr/src/app/dependencies
#apt-get -y install mysql
#RUN apt-get -y update
#RUN dpkg -i /usr/src/app/dependencies/mysql-apt-config_0.8.15-1_all.deb
#RUN apt-get -y update


# Make a port available to communicate with
EXPOSE 5000