pipeline {
    agent none
    stages {
        stage ('Build') {
            agent {
                docker {
                    image 'python:2-alpine'
                }
            }
            steps {
                //sh 'virtualenv venv'
                sh 'source bin/activate'
                sh 'python manage.py test'
                //sh 'pip install -r requirements.txt'
            }
        }
        //stage ('Test') {
        //    agent any
        //    steps {
        //        sh 'python manage.py test'
        //    }
            //post {
            //    always {
            //        junit 'test-reports/results.xml'
            //    }
            //}
       //  }
    }
}
