node {
    stage('SCM Checkout'){
        git 'https://github.com/mallik4ureddy/myprojectrepo.git'
    }
    stage('BUILD Docker Image'){
        powershell label: '', script: 'docker image build -t arjundockerreddy/demo-repository:web1.1.0 .'
    }
    stage('UPLOAD Docker Image'){
        powershell label: '', script: 'docker login -u="arjundockerreddy" -p="docker123"'
        powershell label: '', script: 'docker push arjundockerreddy/demo-repository:web1.1.0'
    }
    stage('RUN Docker container of the Image'){
        withDockerContainer('web1.1.0')
    }
}
