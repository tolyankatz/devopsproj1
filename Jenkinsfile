pipeline {
    agent any
    options {
        skipStagesAfterUnstable()
    }
    stages {
        stage('Build') {
//         agent {
//                 docker {
//                     image: 'docker/dockerfile:1.13'
//                     reuseNode true
//                 }
//             }
            steps {
                sh 'echo "dockers build . -t anatolykatz/mymetrics:1.1.2"'
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
