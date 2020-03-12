pipeline {
    agent any
    stages{
        stage ('Build') {
            steps{
                sh 'cd /Users/rohit.chandwani/test/'
                sh 'source bin/activate'
                sh 'cd /Users/rohit.chandwani/test/projects/telusko'
            }
        }

        stage ('Test') {
            steps {
                sh 'python manage.py test'
            }
        }
    }
}