# Use an official Python runtime as a parent image
FROM python:3.8

# Set the working directory to /app
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY app.py requirements.txt /app/
COPY templates /app/templates
COPY static /app/static

# Install any needed packages specified in requirements.txt
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Set the Flask app environment variable
ENV FLASK_APP=app.py


# Make port 5000 available to the world outside this container
EXPOSE 5000

# Run app.py when the container launches
CMD ["flask", "run", "--host", "0.0.0.0", "--port", "5000"]

