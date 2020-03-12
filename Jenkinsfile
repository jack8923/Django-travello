pipeline {
    agent any
    stages{
        stage ('Build') {
            steps {
                sh 'source bin/activate'
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
