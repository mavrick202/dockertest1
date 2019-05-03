pipeline {
    agent any
    stages {

        stage('Clone Repo') {
            sh 'rm -rf dockertest1'
                    sh 'git clone https://github.com/mavrick202/dockertest1.git'
        }

        stage('Build Docker Image') {
            sh 'cd /var/lib/jenkins/workspace/pipeline2/dockertest1'
            sh ' cp  /var/lib/jenkins/workspace/pipeline2/dockertest1/* /var/lib/jenkins/workspace/pipeline2'
            sh 'docker build -t sreeharshav/pipelinetest:v1 .'
        }

        stage('Push Image to Docker Hub') {
         sh    'docker push sreeharshav/pipelinetest:v1'
        }

        stage('Deploy to Docker Host') {
         sh    'docker -H tcp://10.1.1.200:2375 run --rm -dit --name webapp1 --hostname webapp1 -p 9000:80 --network ansible_nw sreeharshav/pipelinetest:v1'
        }

        stage('Check WebApp Rechability') {
          sh 'curl http://ec2-34-200-220-1.compute-1.amazonaws.com:9000'
        }

    }
}
