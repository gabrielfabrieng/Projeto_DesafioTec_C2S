# Dockerfile for the Python Vehicle Project

FROM python:3.10-slim

# Prevent Python from writing pyc files and buffer stdout/stderr.
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Set the working directory
WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y build-essential && rm -rf /var/lib/apt/lists/*

# Copy dependency list and install Python dependencies
COPY requirements.txt .
RUN pip install --upgrade pip && pip install -r requirements.txt

# Copy the entire project
COPY . .

# Expose the MCP server port
EXPOSE 9999

# Command to run the MCP server as default (can be overridden)
CMD ["python", "mcp_server.py"]
