pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                git branch: 'main', url: 'https://github.com/mrshri07/BCM_modules.git'
            }
        }

        stage('Setup Python Env') {
            steps {
                sh 'python -m venv venv'
                sh './venv/Scripts/activate && pip install -r requirements.txt'
            }
        }

        stage('Run Tests') {
            steps {
                sh './venv/Scripts/activate && pytest tests/'
            }
        }

        stage('Build Complete') {
            steps {
                echo '✅ Build and Tests successful!'
            }
        }
    }
}
