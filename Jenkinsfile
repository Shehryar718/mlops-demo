pipeline {
    agent any

    stages {
        stage('Python Linting') {
            steps {
                sh '''
                    /Users/shehryarsohail-nu/anaconda3/envs/myenv/bin/pip install -r requirements.txt
                    /Users/shehryarsohail-nu/anaconda3/envs/myenv/bin/flake8 . --count --select=E9,F63,F7,F82 --show-source --statistics
                    /Users/shehryarsohail-nu/anaconda3/envs/myenv/bin/flake8 . --count --exit-zero --max-complexity=10 --max-line-length=127 --statistics
                '''
            }
        }

        stage('Python Testing') {
            steps {
                sh '/Users/shehryarsohail-nu/anaconda3/envs/myenv/bin/pytest test.py'
            }
        }
        stage('Deploy') {
            steps {
                script{
                    if (branch_name == "PROD") {
                        println "Deploying to production."
                    } else if (branch_name == "TEST") {
                        println "Deploying to testing."
                    }
                }
            }
        }

        

        
    }
}
