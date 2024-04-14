# Use an official Python runtime as a parent image
FROM python:3.8-slim

 
# Copy the current directory contents into the container at /app
COPY . /app
WORKDIR /app
# Install any needed packages specified in requirements.txt
RUN pip install --upgrade pip
RUN pip install chainlit==1.0.502 openai==1.6.1 open-interpreter==0.2.4
# use openai==1.17.1 for interpreter
# Print the location of tesseract executable
#RUN which tesseract

ENV OPENAI_API_KEY=


EXPOSE 8000

# Run script.py when the container launches
CMD ["python", "create_assistant.py"]
CMD ["chainlit", "run", "./app.py"]
