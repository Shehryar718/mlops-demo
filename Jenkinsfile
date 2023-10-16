pipeline {
    agent any

    stages {
        stage('Python Linting') {
            steps {
                sh '''
                    /Users/shehryarsohail-nu/anaconda3/bin/pip install -r requirements.txt
                    /Users/shehryarsohail-nu/anaconda3/bin/flake8 . --count --select=E9,F63,F7,F82 --show-source --statistics
                    /Users/shehryarsohail-nu/anaconda3/bin/flake8 . --count --exit-zero --max-complexity=10 --max-line-length=127 --statistics
                '''
            }
        }

        stage('Python Testing') {
            steps {
                sh 'pytest test.py'
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
