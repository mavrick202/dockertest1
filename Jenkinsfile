pipeline {
    agent any
    stages {

        stage('Clone Repo') {
          steps {
            sh 'rm -rf dockertest1'
            sh 'git clone https://github.com/mavrick202/dockertest1.git'
            }
        }

        stage('Build Docker Image') {
          steps {
            sh 'cd /var/lib/jenkins/workspace/pipeline2/dockertest1'
            sh 'cp  /var/lib/jenkins/workspace/pipeline2/dockertest1/* /var/lib/jenkins/workspace/pipeline2'
            sh 'docker build -t sreeharshav/pipelinetest:${BUILD_NUMBER} .'
            }
        }

        stage('Push Image to Docker Hub') {
          steps {
           sh    'docker push sreeharshav/pipelinetest:${BUILD_NUMBER}'
           }
        }

        stage('Deploy to Docker Host') {
          steps {
            sh    'docker -H tcp://10.1.1.100:2375 stop webapp1 || true'
            sh    'docker -H tcp://10.1.1.100:2375 run --rm -dit --name webapp1 --hostname webapp1 -p 9000:80 sreeharshav/pipelinetest:${BUILD_NUMBER}'
            }
        }

        stage('Check WebApp Rechability') {
          steps {
          sh 'sleep 10s'
          sh ' curl http://10.1.1.100:9000'
          }
        }

    }
}
