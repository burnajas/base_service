FROM python:3.7

# Docker arguments and defaults (default to `test` environment)
ARG ENVIRONMENT_TYPE="test"
ARG DATABASE_USERNAME=''
ARG DATABASE_PASSWORD=''
ARG DATABASE_URL=''

# Environment variables
ENV ENVIRONMENT_TYPE=$ENVIRONMENT_TYPE
ENV DATABASE_USERNAME=$DATABASE_USERNAME
ENV DATABASE_PASSWORD=$DATABASE_PASSWORD
ENV DATABASE_URL=$DATABASE_URL

# Create a directory for the project code
RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app

# Copy code from host into container
COPY ./code /usr/src/app

# Install packages
#RUN pip3 install --no-cache-dir -r requirements.txt
RUN pip install --no-index --find-links=whl/ -r requirements.txt

# Make a port available to communicate with
EXPOSE 5000
