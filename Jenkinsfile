pipeline {
    agent any
    options {
        skipStagesAfterUnstable()
    }
    stages {
        stage('Build') {
            steps {
                sh 'echo building.....'
                sh 'docker build . -t app'
            }
        }
        stage('Test'){
            steps {
                sh 'echo Test'
                
            }
        }
        stage('Deploy') {
            steps {
                sh 'echo Deploy'
            }
        }
    }
}
