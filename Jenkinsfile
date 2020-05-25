node {
    stage('SCM Checkout'){
        git 'https://github.com/mallik4ureddy/myprojectrepo.git'
    }
    stage('BUILD Docker Image'){
        powershell label: '', script: 'docker image build -t arjundockerreddy/demo-repository:web1.1.0 .'
    }
    stage('PUSH Docker Image to DockerHub'){
    withCredentials([usernameColonPassword(credentialsId: 'docker_creds', variable: 'docker_creds')]) {
      powershell label: '', script: 'docker push arjundockerreddy/demo-repository:web1.1.0'
    }
    }
    stage('RUN Docker image inside a container') {
       def myTestContainer = docker.image('arjundockerreddy/demo-repository:web1.1.0')
       myTestContainer.pull()
    }
}
