pipeline {
    agent {
        docker {
            image 'frolvlad/alpine-python3'
        }
    }
    stages {
        stage ('Build') {
            steps {
                sh 'pip install -r requirements.txt'
                sh 'virtualenv -p python venv'
                sh 'source venv/bin/activate'
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
