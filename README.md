# Co-de-ploy

Co-de-ploy is a hands-on DevOps project for learning and demonstrating
containerization, CI/CD, automated deployment, monitoring, and infrastructure
automation.

## Current Features

- Python Flask application
- Automated tests with pytest
- Docker containerization
- Docker Compose
- Health check endpoint
- Application version endpoint

## Application Endpoints

| Endpoint | Description |
|----------|-------------|
| `/` | Application information |
| `/health` | Application health status |
| `/version` | Application version |

## Run Locally

### Run with Python

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements-dev.txt
python app/app.py