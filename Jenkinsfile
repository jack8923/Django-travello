pipeline {
    agent none
    stages{
        stage ('Build') 
            agent {
                docker {
                    image 'python:2-alpine'
                }
            }
            steps {
                sh 'source bin/activate'
                //sh 'pip install -r requirements.txt'
            }
        }

        stage ('Test') {
            agent {
                docker {
                    image 'qnib/pytest'
                }
            }
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
