pipeline {
    agent any
    stages{
        stage ('Build') {
            steps {
                sh 'source bin/activate'
                sh 'pip install -r requirements.txt'
            }
        }

        stage ('Test') {
            steps {
                sh 'python manage.py test --junit-xml test-reports/results.xml'
            }
            post {
                always {
                    junit 'test-reports/results.aml'
                }
            }
         }
    }
}
