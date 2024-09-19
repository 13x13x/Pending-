# Use an appropriate Python base image
FROM python:3.10

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file into the container
COPY requirements.txt /app/

# Install the Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the entire repository into the container
COPY . /app

# Specify the command to run on container start
CMD ["python3", "bot.py"]
