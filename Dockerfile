# Base image: Python slim
FROM python:3.12-slim

# Set working directory
WORKDIR /app

# Copy simulation + chatbot code
COPY full_cyclekernel_buildA_FH_complete.py /app/
COPY templates/ /app/templates/

# Install dependencies
RUN pip install --no-cache-dir flask flask-socketio eventlet numpy openai

# Expose the port for the dashboard / LLM endpoints
EXPOSE 5000

# Run the simulation server
CMD ["python", "full_cyclekernel_buildA_FH_complete.py"]
