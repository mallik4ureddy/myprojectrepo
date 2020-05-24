node {
    stage('SCM Checkout'){
        git 'https://github.com/mallik4ureddy/myprojectrepo.git'
    }
    stage('BUILD Docker Image'){
        powershell label: '', script: 'docker image build -t arjundockerreddy/demo-repository:web1.1.0 .'
    }
    stage('PUSH Docker Image to DockerHub'){
        powershell label: '', script: 'docker login -u="arjundockerreddy" -p="docker123"'
        powershell label: '', script: 'docker push arjundockerreddy/demo-repository:web1.1.0'
    }
    stage('PULL Docker image from DockerHub'){
        powershell label: '', script: 'docker pull arjundockerreddy/demo-repository:web1.1.0'
    }
    stage('RUN Docker Container with the Image'){
        powershell label: '', script: 'docker container run -it arjundockerreddy/demo-repository:web1.1.0'
    }
}
