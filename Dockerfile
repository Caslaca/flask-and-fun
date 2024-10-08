# Use the official Python base image
FROM python:3.12-slim

# Set the working directory in the container
WORKDIR /app

# Copy the application code to the container
COPY . /app

# Install setuptools
RUN pip install --no-cache-dir setuptools

# Install the application dependencies
RUN python setup.py install

# Expose the port on which the Flask app will run
EXPOSE 5000
# Set the environment variable for Flask app
ENV FLASK_APP=hello
# Set the entrypoint command to run the Flask app
CMD ["flask", "run", "--host=0.0.0.0"]