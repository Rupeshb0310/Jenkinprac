pipeline {
    agent any
    stages {
        stage('Clone sources') {
            steps {
                git url: 'https://github.com/Rupeshb0310/python-tutorial.git'
            }
        }
        stage('DEmo') {
            steps {
                sh "pip install coverage"
                sh "pip3 install coverage"
            }
        }
        stage('SonarQube analysis') {
            steps {
                script{
                    def scannerHome = tool 'Sonarqube-9.5';

                    withSonarQubeEnv('Sonarqube-9.5') {
                      sh "${scannerHome}/bin/sonar-scanner \
                      -D sonar.projectKey=coverage \
                      -D sonar.host.url=http://localhost:9000/"
                  }
                }
    }
  }
       
    }
}
