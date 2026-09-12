README.md — Jenkins Pipeline Demo
Overview
This repository contains a simple Flask application and a Jenkins Pipeline used to demonstrate CI/CD automation. The pipeline builds the application, installs dependencies, optionally builds a Docker image, and can be extended to deploy to any environment.

The project is designed to be lightweight and ideal for learning Jenkins Pipelines, SCM polling, and automated builds.

Project Structure
Code
.
├── app.py
├── requirements.txt
├── Dockerfile        (optional)
└── Jenkinsfile
app.py
A minimal Flask API with a root endpoint and a /health endpoint.

requirements.txt
Python dependencies required for the application.

Jenkinsfile
Defines the CI/CD pipeline stages executed by Jenkins.

Prerequisites
Before running the pipeline, ensure the following:

Jenkins is installed and running

Jenkins has access to your Git repository

Python 3.x is installed on the Jenkins agent

(Optional) Docker is installed if you plan to build container images

Jenkins user is added to the Docker group (if using Docker):

Code
sudo usermod -aG docker jenkins
sudo systemctl restart jenkins
Pipeline Stages
The Jenkins Pipeline includes the following stages:

1. Checkout
Pulls the latest code from your Git repository.

2. Install Dependencies
Installs Python packages from requirements.txt:

Code
pip install -r requirements.txt
3. Run Application Tests (optional)
You can add unit tests here.

4. Build Docker Image (optional)
Builds a Docker image for the Flask app:

Code
docker build -t demo-flask-app .
5. Deploy (optional)
Deploys the application or pushes the Docker image to a registry.

Sample Jenkinsfile
groovy
pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Install Dependencies') {
            steps {
                sh 'pip install -r requirements.txt'
            }
        }

        stage('Build Docker Image') {
            steps {
                sh 'docker build -t demo-flask-app .'
            }
        }

        stage('Deploy') {
            steps {
                echo 'Deployment step goes here'
            }
        }
    }
}
Running the Application Locally
Install dependencies:

Code
pip install -r requirements.txt
Run the app:

Code
python app.py
Access it in your browser:

Code
http://localhost:5000
Health check:

Code
http://localhost:5000/health
SCM Polling
Your Jenkins job supports SCM polling to automatically trigger builds when changes are pushed to the repository.

Example schedule (every 2 minutes):

Code
H/2 * * * *
Extending the Pipeline
You can enhance this pipeline by adding:

Unit tests

Docker push to Docker Hub or GHCR

Kubernetes deployment

Notifications (Slack, Teams, Email)

Multi-branch pipeline support

License
This project is for educational and demonstration purposes.
