pipeline{
    agent any
    tools{
        maven "maven-3.6"
    }
    stages{
       stage('GetCode'){
            steps{
                echo "code download"
            }
         }        
       stage('Build'){
            steps{
                sh 'python sq.py'
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
