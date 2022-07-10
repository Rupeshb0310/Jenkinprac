pipeline {
    agent any
    stages {
        stage('Clone sources') {
            steps {
                git url: 'https://github.com/Rupeshb0310/Jenkinprac.git'
            }
        }
        stage('DEmo') {
            steps {
                sh "pip install coverage"
                sh "pip3 install coverage"
                sh "ls"
                sh "coverage run factorial_test.py"
                sh "coverage report"
                sh "coverage xml"
                sh "ls"
            }
        }
        stage('SonarQube analysis') {
            steps {
                script{
                    def scannerHome = tool 'Sonarqube-9.5';
                    sh "ls"

                    withSonarQubeEnv('Sonarqube-9.5') {
                      sh "${scannerHome}/bin/sonar-scanner \
                      -D sonar.python.version=1.0 \
                      -D sonar.projectKey=coverage \
                      -D sonar.host.url=http://localhost:9000/"
                  }
                }
    }
  }
       
    }
}
