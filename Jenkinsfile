pipeline {
    agent {
        docker {
            //image 'circleci/python:3.6'//'python:3-alpine'
            image 'rohitchandwani/pythonimg'
        }
    }
    stages {
        stage ('Test') {
            steps {
                //sh 'source bin/activate'
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
