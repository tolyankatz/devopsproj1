pipeline {
    agent any
    options {
        skipStagesAfterUnstable()
    }
    stages {
        stage('Build') {

            steps {
                sh 'echo "docker build . -t anatolykatz/mymetrics:1.1.2"'
            }
        }
        stage('Test'){
            steps {
                sh 'echo "pytest ."'
                
            }
        }
        stage('Deploy') {
            steps {
                sh 'echo "deploy"'
            }
        }
    }
}
