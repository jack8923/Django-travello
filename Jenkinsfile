pipeline {
    agent {
        docker {
            image 'python:2-alpine'
        }
    }
    stages {
        stage ('Build') {
            steps {
                sh 'virtualenv -p python venv'
                sh 'source venv/bin/activate'
                //sh 'python manage.py test'
                sh 'pip install -r requirements.txt'
            }
        }
        stage ('Test') {
            steps {
                sh 'python manage.py test'
            }
            //post {
            //    always {
            //        junit 'test-reports/results.xml'
            //    }
            //}
        }
    }
}
