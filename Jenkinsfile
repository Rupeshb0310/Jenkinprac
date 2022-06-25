pipeline{
    agent any
    tools{
        maven "maven-3.6"
    }
    stages{
           
       stage('Build'){
            steps{
                sh 'python3 sq.py'
            }
         }
        stage('SonarQube analysis') {
//    def scannerHome = tool 'SonarScanner 4.0';
            def scannerHome = tool 'Sonarqube-9.5';
        steps{
            
            withSonarQubeEnv('Sonarqube-9.5') {
            sh "${scannerHome}/bin/sonar-scanner"
    }
        }
        }
       
    }
}
