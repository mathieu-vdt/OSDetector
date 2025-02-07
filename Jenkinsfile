pipeline {
    agent any
    stages {
        stage('Clonage du dépôt GitHub') {
            steps {
                git branch: 'main', url: 'https://github.com/mathieu-vdt/OSDetector.git'
            }
        }
        stage('Installation de Python 3 et pip') {
            steps {
                sh 'sudo apt update && sudo apt install -y python3 python3-pip'
            }
        }
        stage('Exécution du script Python') {
            steps {
                sh 'python3 script.py'
            }
        }

        post {
        always {
            emailext subject: "Jenkins Build: ${currentBuild.fullDisplayName}",
                     body: "Le build ${currentBuild.currentResult} est terminé.\n\nConsultez les logs ici : ${env.BUILD_URL}",
                     to: 'luckylebg@oui.com'
        }
    }
    }
}
