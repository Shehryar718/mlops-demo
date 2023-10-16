pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }
        stage('Checking python') {
            steps {
                sh 'whereis python'
            }
        }
        stage('Python Linting') {
            steps {
                sh '''
                    python -m pip install --upgrade pip
                    pip install flake8 pytest
                    if [ -f requirements.txt ]; then pip install -r requirements.txt; fi
                    flake8 . --count --select=E9,F63,F7,F82 --show-source --statistics
                    flake8 . --count --exit-zero --max-complexity=10 --max-line-length=127 --statistics
                '''
            }
        }

        stage('Python Testing') {
            steps {
                sh 'python -m pip install --upgrade pip'
                sh 'pip install flake8 pytest'
                sh 'if [ -f requirements.txt ]; then pip install -r requirements.txt; fi'
                sh 'make test'
            }
        }
    }

    post {
        success {
            echo 'Pipeline successful!'
        }
        failure {
            echo 'Pipeline failed.'
        }
    }
}
