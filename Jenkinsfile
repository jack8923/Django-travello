pipeline {
    agent any
    stages {
        stage ('Build') {
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
