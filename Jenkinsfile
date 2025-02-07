pipeline {
    agent any

    stages {
        stage('Clonage du dépôt GitHub') {
            steps {
                script {
                    try {
                        git branch: 'main', url: 'https://github.com/mathieu-vdt/OSDetector.git'
                    } catch (Exception e) {
                        echo "⚠️ Erreur lors du clonage : ${e}"
                        currentBuild.result = 'UNSTABLE'
                    }
                }
            }
        }

        stage('Installation de Python 3.11 et pip') {
            steps {
                script {
                    try {
                        sh 'apt update && apt install -y python3.11 python3-pip'
                    } catch (Exception e) {
                        echo "⚠️ Erreur lors de l'installation de Python : ${e}"
                        currentBuild.result = 'UNSTABLE'
                    }
                }
            }
        }

        stage('Exécution du script Python') {
            steps {
                script {
                    try {
                        sh 'python3.11 script.py'
                    } catch (Exception e) {
                        echo "⚠️ Erreur lors de l\'exécution du script : ${e}"
                        currentBuild.result = 'UNSTABLE'
                    }
                }
            }
        }
    }
}
