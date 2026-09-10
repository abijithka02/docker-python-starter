# 🐳 YouTube Docker Series — Python Containerization Hands-on

Welcome to the companion repository for the **Docker Series**! This repository is designed as a clean, beginner-friendly starting point for students to practice **containerizing a Python application with Docker**.

---

## 📌 Repository Overview

This repository contains a simple, long-running Python script ([script.py](file:///Users/abijithka/Code/self/Youtube-Docker-Series/script.py)) simulating a service or worker process.

### Project Structure
```text
Youtube-Docker-Series/
├── script.py          # Python source script
└── README.md          # Project guide & instructions
```

---

## 🔍 Understanding the Application

Take a look at [script.py](file:///Users/abijithka/Code/self/Youtube-Docker-Series/script.py):

```python
import time

print("🚀 Started")

try:
    while True:
        print("Hello World")
        time.sleep(5)

except KeyboardInterrupt:
    print("\n🛑 Shutdown requested. Exiting gracefully...")
```

### What does it do?
- **Starts up**: Prints a startup message (`🚀 Started`).
- **Heartbeat loop**: Prints `"Hello World"` every 5 seconds.
- **Graceful shutdown**: Catches `KeyboardInterrupt` (`Ctrl+C` or `SIGINT`) to cleanly exit with `🛑 Shutdown requested. Exiting gracefully...`.

---

## 💻 Running Locally (Without Docker)

Before containerizing, verify the script works on your local machine:

### Prerequisites
- Python 3.8 or higher installed on your machine.

### Run Command
```bash
python3 script.py
```

### Expected Output
```text
🚀 Started
Hello World
Hello World
...
```
Press `Ctrl + C` in your terminal to see the graceful exit message:
```text
🛑 Shutdown requested. Exiting gracefully...
```

---

## 🎯 Student Assignment: Containerize This Application

Your goal is to package this Python script into a Docker container image so it can run predictably in any environment.

### Requirements for your container:
1. Choose an appropriate base image (e.g., official `python:3.11-slim` or `python:3.12-alpine`).
2. Set a working directory inside the container (e.g., `/app`).
3. Copy [script.py](file:///Users/abijithka/Code/self/Youtube-Docker-Series/script.py) into the container's working directory.
4. Configure the container to execute `python script.py` when started.
5. Ensure Python output is unbuffered so log lines appear in real-time.

---

## 🛠️ Step-by-Step Guide & Hints

### 1. Create a `Dockerfile`
In the root of this project directory, create a file named `Dockerfile` (no file extension).

A recommended structure:
```dockerfile
# Step 1: Use an official lightweight Python image
FROM python:3.11-slim

# Step 2: Set environment variables
# Prevents Python from buffering stdout/stderr (crucial for Docker logs!)
ENV PYTHONUNBUFFERED=1

# Step 3: Set working directory inside container
WORKDIR /app

# Step 4: Copy application code into container
COPY script.py .

# Step 5: Specify command to execute
# Note: Use JSON array format (exec form) so signals like SIGTERM reach Python!
CMD ["python", "script.py"]
```

### 2. Build the Docker Image
Run the following command in your terminal from the repository folder:

```bash
docker build -t python-docker-demo:v1 .
```

- `-t python-docker-demo:v1`: Tags your image with a friendly name and version tag.
- `.`: Sets the build context to the current directory.

### 3. Run Your Docker Container

#### Option A: Run Interactively (Foreground)
See logs directly in your console:
```bash
docker run --rm -it python-docker-demo:v1
```
*(Press `Ctrl + C` to stop the container.)*

#### Option B: Run in Detached Mode (Background)
Run the container in the background as a named daemon:
```bash
docker run -d --name my-python-app python-docker-demo:v1
```

### 4. Check Container Logs
If running in background mode, inspect the live logs:
```bash
docker logs -f my-python-app
```

### 5. Stop and Remove the Container
```bash
# Stop the container
docker stop my-python-app

# Remove the container
docker rm my-python-app
```

---

## 💡 Key Docker Concepts to Keep in Mind

> [!IMPORTANT]
> **Python Log Buffering (`PYTHONUNBUFFERED=1`)**  
> In Docker, if Python buffers standard output, you won't see `print()` logs immediately when running `docker logs`. Setting `ENV PYTHONUNBUFFERED=1` or running `python -u script.py` ensures real-time logging.

> [!TIP]
> **Exec Form vs Shell Form (`CMD`)**  
> Prefer exec syntax: `CMD ["python", "script.py"]` instead of `CMD python script.py`.  
> Shell form launches `/bin/sh -c` as PID 1, which might intercept and swallow termination signals (`SIGTERM`), preventing graceful shutdown.

> [!TIP]
> **Use Slim or Alpine Base Images**  
> Always prefer minimal base images like `python:3.x-slim` over full images (`python:3.x`) to keep image sizes small and reduce security vulnerabilities.

---

## 🚀 Extra Challenges for Students

Once you have the basic container running:
- [ ] Add a `.dockerignore` file to prevent unwanted files/folders (like `.git`, `.venv`, `__pycache__`) from being copied into the build context.
- [ ] Run the container as a non-root user for security best practices.
- [ ] Create a `docker-compose.yml` file to manage and spin up the service.
