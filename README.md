This project explores advanced Docker logging mechanisms, log rotation, external logging drivers, and log aggregation using the ELK (Elasticsearch, Logstash, Kibana) stack. The goal is to manage, rotate, and visualize logs from Docker containers.

## Features
- **Sample Flask Web Application**: Generates logs of various levels (INFO, DEBUG, ERROR).
- **Log Rotation**: Prevents log files from growing indefinitely.
- **External Logging Drivers**: Logs are sent to `syslog` or `gelf`.
- **ELK Stack Setup**: Aggregates and visualizes logs from multiple containers.
- **Multi-container Logging**: Logging for both Flask and MySQL containers.

## Prerequisites
- Docker
- Docker Compose

## Usage

### Step 1: Build and Run Flask Application
```bash
docker build -t flask-log-app .
docker run -d -p 5000:5000 --name flask-log-app flask-log-app
```

### Step 2: Inspect Logs
View container logs:
```bash
docker logs flask-log-app
```

Stream logs in real-time:
```bash
docker logs -f flask-log-app
```

### Step 3: Set Up Log Rotation
```bash
docker run -d --name flask-log-app \
  --log-opt max-size=10m \
  --log-opt max-file=3 \
  flask-log-app
```

### Step 4: Use ELK Stack for Log Aggregation
Start the ELK stack:
```bash
docker-compose up -d
```
Access Kibana at `http://localhost:5601`.

### Step 5: Configure External Logging Driver
Run the container with the GELF log driver:
```bash
docker run -d --log-driver=gelf --log-opt gelf-address=udp://localhost:5044 flask-log-app
```

### Step 6: Multi-container Setup
Add another service (e.g., MySQL) to the `docker-compose.yml` file and aggregate logs from both containers.

## ELK Stack Setup
To run the ELK stack, ensure the following services are running:
- Elasticsearch (`localhost:9200`)
- Logstash (`localhost:5044`)
- Kibana (`localhost:5601`)
