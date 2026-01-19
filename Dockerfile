# Base image: Python slim
FROM python:3.12-slim

# Set working directory
WORKDIR /app

# Copy requirements and install dependencies
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

# Copy simulation + chatbot code
COPY full_cyclekernel_buildA_FH_complete.py /app/
COPY templates/ /app/templates/

# Expose the port for the dashboard / LLM endpoints
EXPOSE 5000

# Run the simulation server
CMD ["python", "full_cyclekernel_buildA_FH_complete.py"]
