
pipeline {
    agent any
    stages {
        stage('Clone sources') {
            steps {
                
                checkout poll: false, 
                    scm: [$class: 'GitSCM',
                          branches: [[name: '*/master']],
                          extensions: [[$class: 'RelativeTargetDirectory', relativeTargetDir: 'master']],
                          userRemoteConfigs: [[credentialsId: 'Github',
                          url: 'https://github.com/Rupeshb0310/Jenkinprac.git']]
                    ]
            }
        }
        stage('DEmo') {
            steps {
                sh "pip install coverage"
                sh 'ls'
                sh """
                #!/bin/bash
                 set -e
                 cd /var/lib/jenkins/.local/lib/python3.8/
                 coverage report
            
                    """
                
            
            }
        }
        stage('SonarQube analysis') {
            steps {
                script{
                    def scannerHome = tool 'Sonarqube-9.5';
                    

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
