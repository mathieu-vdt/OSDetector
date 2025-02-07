pipeline {
    agent any
    stages {
        stage('Build') {
            steps {
                script {
                    // Vérification du type de système d'exploitation
                    if (isUnix()) {
                        // Si Unix, exécuter la commande 'make' via 'sh'
                        sh 'make'
                    } else {
                        // Si autre type de système (probablement Windows), exécuter via 'bat'
                        bat 'make'
                    }
                }
            }
        }

        stage('Permissions') {
            when {
                expression { return isUnix() } // Cette étape ne s'exécute que si le système est Unix
            }
            steps {
                script {
                    // Donner les droits d'exécution au binaire résultant
                    sh 'chmod +x <nom_du_binaire>' // Remplacez '<nom_du_binaire>' par le nom réel du binaire
                }
            }
        }

        stage('Nettoyage') {
            steps {
                script {
                    // Exécution de la commande 'make clean'
                    if (isUnix()) {
                        sh 'make clean'
                    } else {
                        bat 'make clean'
                    }
                }
            }
        }
    }
}