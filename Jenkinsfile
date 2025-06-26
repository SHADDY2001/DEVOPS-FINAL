pipeline {
    agent any

    stages {
        stage('Clone GitHub Repo') {
            steps {
                git 'https://github.com/SHADDY2001/DEVOPS-FINAL.git'
            }
        }

        stage('Build Docker Image') {
            steps {
                bat 'wsl docker build -t jenkins-devops-app .'
            }
        }
    }
}
