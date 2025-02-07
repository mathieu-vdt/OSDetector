pipeline {
    agent any
    stages {
        stage('Clonage du dépôt GitHub') {
            steps {
                git branch: 'main', url: 'https://github.com/mathieu-vdt/OSDetector.git'
            }
        }
        stage('Installation de Python 3.11 et pip') {
            steps {
                sh 'echo "jenkins-password" | sudo -S apt update && sudo -S apt install -y python3.11 python3-pip'
            }
        }
        stage('Exécution du script Python') {
            steps {
                sh 'python3 script.py'
            }
        }
    }
}
