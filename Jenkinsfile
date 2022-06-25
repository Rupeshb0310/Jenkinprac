pipeline{
    agent any
    tools{
        maven "maven-3.6"
    }
    stages{
       stage('GetCode'){
            steps{
                git 'https://github.com/Rupeshb0310/Jenkinprac.git'
            }
         }        
       stage('Build'){
            steps{
                sh 'python3 sq.py'
            }
         }
    stage('SonarQube Analysis') {
    def scannerHome = tool 'Sonarqube-9.5'
      withSonarQubeEnv('Sonarqube-9.5') {
      sh """/var/lib/jenkins/tools/hudson.plugins.sonar.SonarRunnerInstallation/SonarQube/bin/sonar-scanner \
     -D sonar.projectVersion=1.0-SNAPSHOT \
       -D sonar.login=admin \
      -D sonar.password=0000 \
      -D sonar.projectBaseDir=/var/lib/jenkins/workspace/jenkins-sonar/ \
        -D sonar.projectKey=pysq \
        -D sonar.sourceEncoding=UTF-8 \
        -D sonar.language=py \
        -D sonar.sources=my-app/src/main \
        -D sonar.tests=my-app/src/test \
        -D sonar.host.url=http://localhost:9000/"""
        }
}
       
    }
}
