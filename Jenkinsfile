// Jenkinsfile

pipeline {
    agent any

    stages {
        stage('Clone Repository') {
            steps {
                checkout([$class: 'GitSCM', branches: [[name: '*/main']], userRemoteConfigs: [[url: 'https://github.com/apiwizlabs/wizdesk.git']]])
            }
        }

        stage('Build and Test') {
            steps {
                script {
                    sh 'mvn clean package'
                }
            }
        }

        stage('Build Docker Image') {
            steps {
                script {
                    sh 'docker build -t sunildocker786/wizdesk:${BUILD_NUMBER} .'
                }
            }
        }

        stage('Publish to Docker Registry') {
            steps {
                script {
                    sh 'docker push sunildocker786/wizdesk:${BUILD_NUMBER}'
                }
            }
        }

        stage('Deploy to Kubernetes') {
            steps {
                script {
                    sh 'kubectl apply -f k8s/deployment.yaml'
                }
            }
        }
    }
}
