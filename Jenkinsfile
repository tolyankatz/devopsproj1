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
                sh 'echo "docker build . -t anatolykatz/mymetrics:1.1.2"'
                sh 'echo "check build "'
            }
        }
        stage('Test'){
            steps {
                sh 'echo "pytest_1 ."'
                
            }
        }
        stage('Deploy') {
            steps {
                sh 'echo "deploy_2"'
            }
        }
    }
}
