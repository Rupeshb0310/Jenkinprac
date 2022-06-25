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

            
        steps{
            
            withSonarQubeEnv('Sonarqube-9.5') {
            sh "Sonarqube-9.5/bin/sonar-scanner"
    }
        }
        }
       
    }
}
