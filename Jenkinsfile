pipeline {
    agent any

    stages {
        stage('Python Linting') {
            steps {
                tool name: 'Python 3.8', type: 'hudson.plugins.python.PythonInstallation' // Use the name of your Python tool installation
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
                tool name: 'Python 3.8', type: 'hudson.plugins.python.PythonInstallation' // Use the name of your Python tool installation
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
