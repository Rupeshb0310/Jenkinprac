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
        stage('SonarQube analysis') {
//    def scannerHome = tool 'SonarScanner 4.0';
        steps{
        withSonarQubeEnv('Sonarqube 9.5') { 
        // If you have configured more than one global server connection, you can specify its name
//      sh "${scannerHome}/bin/sonar-scanner"
        sh "mvn sonar:sonar"
    }
        }
        }
       
    }
}