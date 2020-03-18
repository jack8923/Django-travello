pipeline {
    agent {
        docker {
            //image 'circleci/python:3.6'//'python:3-alpine'
            image 'rohitchandwani/pythonimg'
        }
    }
    stages {
        //stage ('Build') {
        //    steps {
        //        sh 'python3 -m venv venv'
        //        sh '. venv/bin/activate'
        //        sh 'pip3 install --user -r requirements.txt'
                //sh 'python manage.py test'
        //          sh 'python -m pip install Django'
        //    }
        //}
        stage ('Test') {
            steps {
                sh 'source bin/activate'
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
