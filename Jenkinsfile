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
      stage('Build') { 
            agent {
                docker {
                    image 'python:2-alpine' 
                }
            }}
            steps {
                sh 'python -m py_compile sources/add2vals.py sources/calc.py' 
                stash(name: 'compiled-results', includes: 'sources/*.py*') 
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
