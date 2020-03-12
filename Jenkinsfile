pipeline {
    agent {
        docker {
            image 'circleci/python:3.6'//'python:3-alpine'
        }
    }
    stages {
        stage ('Build') {
            steps {
                sh 'python3 -m venv venv'
                sh 'source venv/bin/activate'
                sh 'pip install -r requirements.txt'
                sh 'python manage.py test'
              
            }
        }
        //stage ('Test') {
            //steps {
                
            //}
            //post {
            //    always {
            //        junit 'test-reports/results.xml'
            //    }
            //}
        //}
    }
}
