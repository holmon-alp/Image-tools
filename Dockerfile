# FROM python:3.11.7

# ENV PYTHONUNBUFFERED True

# EXPOSE 8080

# RUN apt-get -y update && apt-get -y install tesseract-ocr

# ENV APP_HOME /app

# WORKDIR $APP_HOME

# COPY . ./

# RUN pip install -r requirements.txt

# # CMD streamlit run --server.port 8080 --server.enableCORS false app.py
# ENTRYPOINT ["streamlit", "run", "app.py", "--server.port=8080", "--server.address=0.0.0.0"]

# Use an official Python runtime as a parent image
FROM python:3.11

# Set the working directory in the container to /app
WORKDIR /app

# Install any needed packages specified in requirements.txt
RUN apt-get update && apt-get install -y \
    tesseract-ocr \
    && rm -rf /var/lib/apt/lists/*

# Clone your Streamlit app from a repository (if not in the same directory as Dockerfile)
# RUN git clone https://github.com/holmon-alp/Image-tools.git .

# If your app is in the same directory as the Dockerfile, use COPY instead of git clone
COPY . .

# Install any needed packages specified in requirements.txt
RUN pip3 install -r requirements.txt

# Make port  8501 available to the world outside this container



# Define a health check command to let Docker know if your app is running
HEALTHCHECK CMD curl --fail http://localhost:8501/_stcore/health

# Run streamlit when the container launches
ENTRYPOINT ["streamlit", "run", "   app.py", "--server.port=8501", "--server.address=0.0.0.0"]
