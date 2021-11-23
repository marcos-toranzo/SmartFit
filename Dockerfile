FROM python:alpine3.14

# Update container repository -> Create tester user -> 
# install make for task management ->
# install pytest for running tests -> delete pip
RUN apk update && apk upgrade \
    && adduser -D tester \
    && apk add make \
    && pip install pytest \
    && python3 -m pip uninstall pip -y

# Use tester user with no root privileges
USER tester

# Set test directory
WORKDIR /app/test

# Copy task manager file
COPY Makefile .

# Copy app code
COPY smartfit ./smartfit

# Copy tests
COPY tests ./tests

# Run tests
CMD ["make", "test"]