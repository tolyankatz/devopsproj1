pipeline {
    agent any
    options {
        skipStagesAfterUnstable()
    }
    stages {
        stage('Build') {
            steps {
                sh 'echo building.....'
                build("anatolykatz/mymetrics:1.1.2")
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
