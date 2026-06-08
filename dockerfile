FROM python:3.11
WORKDIR /app
COPY . .
CMD ["python", "Bank_system_project.py"]