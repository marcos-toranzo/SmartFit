FROM python:alpine3.14

# Create tester user -> install make for task management ->
# create test directory -> set permission for tester user ->
# install pytest for running tests -> delete pip
RUN adduser -D tester \  
    && apk add make \
    && mkdir -p /app/test \
    && chown tester /app/test \
    && pip install pytest \
    && python3 -m pip uninstall pip -y

# Use tester user with no root privileges
USER tester

# Set test directory
WORKDIR /app/test

# Copy task manager file
COPY Makefile .

# Run tests
CMD ["make", "test"]