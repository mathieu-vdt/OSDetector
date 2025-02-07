pipeline {
    agent any
    stages {
        stage('Clonage du dépôt GitHub') {
            steps {
                git branch: 'main', url: 'https://github.com/mathieu-vdt/OSDetector.git'
            }
        }
        stage('Exécution du script Python') {
            steps {
                sh 'python3 script.py'
            }
        }
    }
}
