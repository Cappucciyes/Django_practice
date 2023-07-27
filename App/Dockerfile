# Pull base image
FROM python:3.11.3

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set work directory
WORKDIR /code

# Install dependencies
COPY requirements.txt requirements.txt 
RUN pip install -r requirements.txt

# Copy project
# Copy everything from App folder(first '.') to /code (second '.')
COPY . . 

# Run command below so when docker is running so will be our project
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
