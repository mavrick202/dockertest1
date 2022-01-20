pipeline {
    environment {
        registry = 'sreeharshav/devopsb22dev'
        registryCredential = 'dockerhub_id'
        devcontext = 'dev-swarm'
        prodcontext = 'prod-swarm'
        devnode = '10.40.1.237'
        prodnode = '10.40.1.149'
        dockerImage = ''
    }
    agent any
    stages {
        stage('Building Dev Docker Branch') {
            when {
                    GIT_BRANCH = 'origin/' + sh(returnStdout: true, script: 'git rev-parse --abbrev-ref HEAD').trim()
                    return GIT_BRANCH == 'origin/DevOpsB22-Dev'
            }
        }
        stage('Building our image') {
            steps {
                script {
                    dockerImage = docker.build registry + ":v$BUILD_NUMBER"
                }
            }
        }
        stage('Push Image To DockerHUB') {
            steps {
                script {
                    docker.withRegistry( '', registryCredential ) {
                        dockerImage.push()
                    }
                }
            }
        }
        stage('Cleaning up') {
            steps {
                sh "docker rmi $registry:v$BUILD_NUMBER"
            }
        }
        stage('Deploying to Dev Docker Swarm') {
            steps {
                sh "docker context use $devcontext"
                sh 'docker service rm testing1 || true'
                sh "docker service create --name testing1 -p 8100:80 $registry:v$BUILD_NUMBER"
            }
        }
        stage('Verifying The Deployment') {
            steps {
                sh 'curl http://devnode:8100 || exit 1'
            }
        }
    }
}
