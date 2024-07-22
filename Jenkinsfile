pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                git branch: 'main', url: 'https://github.com/csurqunix/OSDetector.git'
            }
        }

        stage('Build') {
            steps {
                sh 'chmod +x OSDetector.py'
                sh 'python3 OSDetector.py'
            }
        }
    }

    post {
        success {
            echo 'Build and script execution succeeded!'
        }
        failure {
            echo 'Build or script execution failed.'
            script {
                def emailBody = "Bonjour,\n\nLa construction et l'exécution du script ont échoué. Veuillez vérifier les journaux de construction Jenkins pour plus de détails.\n\nCordialement,\nL'équipe DevOps"
                emailext (
                    subject: 'Échec de la construction Jenkins',
                    body: emailBody,
                    recipientProviders: [[$class: 'CulpritsRecipientProvider']],
                    to: 'cedsurq@protonmail.com'
                )
            }
        }
    }
}
