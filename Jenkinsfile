pipeline {
    agent any
    stages {
        stage ('Build') {
            steps {
                sh 'virtualenv venv'
                sh 'source venv/bin/activate'
                sh 'pip install -r requirements.txt'
            }
        }
        stage ('Test') {
            agent any
            steps {
                sh 'python manage.py test --junit-xml test-reports/results.xml'
            }
            post {
                always {
                    junit 'test-reports/results.xml'
                }
            }
         }
    }
}