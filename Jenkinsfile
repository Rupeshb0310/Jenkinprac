pipeline {
    agent any
    stages {
        stage('Clone sources') {
            steps {
                git url: 'https://github.com/Rupeshb0310/Jenkinprac.git'
            }
        }
        stage('SonarQube analysis') {
            steps {
                script{
                    def scannerHome = tool 'Sonarqube-9.5';

                    withSonarQubeEnv('Sonarqube-9.5') {
                      sh "${scannerHome}/bin/sonar-scanner \
                      -D sonar.host.url=http://localhost:9000/ \
                      -D sonar.projectKey=demo \
                      -D sonar.python.coverage.reportPaths=/sonarqube-flask/coverage.xml \
                      -D sonar.python.xunit.reportPath=/sonarqube-flask/result.xml \
                      -D sonar.coverage.dtdVerification=false \
                      -D sonar.inclusions=app.py \
                      -D sonar.coverage.exclusions=**/__init__.py "
                      
                  }
                }
    }
  }
       
    }
}
