node {
    stage('SCM Checkout'){
        git 'https://github.com/mallik4ureddy/myprojectrepo.git'
    }
    stage('Build Docker Image'){
      sh 'docker image build -t arjundockerreddy/demo-repository:web1.1.0 .'

    }
}
