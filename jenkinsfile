pipeline {
    agent any

    stages {
        stage('Clone Repo') {
            steps {
                // Jenkins clones your GitHub repo here
                git credentialsId: 'github-pat', url: 'https://github.com/sabanazneenn/calci-cicd.git'
            }
        }

        stage('Build Docker Image') {
            steps {
                script {
                    sh 'docker build -t flask-bash-calculator .'
                }
            }
        }

        stage('Run Docker Container') {
            steps {
                script {
                    // Stop and remove existing container if it's already running
                    sh 'docker rm -f calci-app || true'
                    sh 'docker run -d -p 5001:5000 --name calci-app flask-bash-calculator'
                }
            }
        }
    }
}
