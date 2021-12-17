FROM python:3.9-slim

# Update container repository -> Create tester user -> 
# install make for task management ->
# install pytest for running tests -> delete pip
RUN apt-get update && apt-get upgrade -y \
    && useradd -ms /bin/bash tester \
    && apt-get install make \
    && pip install pytest "fastapi[all]" "uvicorn[standard]" \
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