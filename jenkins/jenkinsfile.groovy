def lastCommit
def latestVersion

pipeline {

    agent {
        label 'docker-node'
        }
    stages {
        stage('Build Docker image') {
            steps {
                dir('./'){
                    script {
                        sh "sudo chmod 777 Dockerfile"
                        sh "sudo docker build -t foodproj ."
                    }
                }
            }
        }
        stage('Test Docker image') {
            steps {
                dir('./tests') {
                    script{
                       sh "sudo chmod 755 basic.test.sh"
                       sh "sudo ./basic.test.sh"
                    }
                }
            }
        }
        stage('Upload image to repository') {
            steps {
                sh "pwd"
            }
        }
        stage('Deploy to Prod') {
            steps {
                script {
                    dir('deployment') {
                        println("continue")
            }
        }
    }
}
