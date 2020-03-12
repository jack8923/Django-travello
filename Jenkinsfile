pipeline {
    agent {
        docker {
            image 'python:3-alpine'
        }
    }
    stages {
        stage ('Build') {
            steps {
                sh 'virtualenv -p python venv'
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
