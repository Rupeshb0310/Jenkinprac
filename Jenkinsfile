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
                      -D sonar.projectKey=sqcv \
                      -D sonar.python.coverage.reportPaths=coverage.xml \
                      -D sonar.host.url=http://localhost:9000/"
                  }
                }
    }
  }
       
    }
}
