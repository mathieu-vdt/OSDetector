import os
import sys
import platform
import docker
from docker.errors import ContainerError, ImageNotFound

# Vérifier le système d'exploitation
def is_unix():
    return platform.system().lower() in ['linux', 'darwin']  # Linux ou macOS

# Création d'un client Docker
def get_docker_client():
    return docker.from_env()

# Fonction pour créer et démarrer un conteneur Docker
def create_and_start_container(client, image_name, container_name, ports=None):
    try:
        print(f"Création et démarrage du conteneur '{container_name}' à partir de l'image '{image_name}'...")
        
        # Vérifier si l'image existe localement, sinon tenter de la télécharger
        try:
            client.images.get(image_name)
        except ImageNotFound:
            print(f"L'image '{image_name}' introuvable localement. Téléchargement de l'image...")
            client.images.pull(image_name)
        
        # Lancer le conteneur
        container = client.containers.run(image_name, name=container_name, ports=ports, detach=True)
        print(f"Conteneur '{container_name}' démarré avec succès.")
        return container
    except Exception as e:
        print(f"Erreur lors de la création et du démarrage du conteneur : {e}")

# Fonction pour arrêter un conteneur
def stop_container(client, container_name):
    try:
        container = client.containers.get(container_name)
        container.stop()
        print(f"Conteneur '{container_name}' arrêté.")
    except Exception as e:
        print(f"Erreur lors de l'arrêt du conteneur : {e}")

# Fonction pour supprimer un conteneur
def remove_container(client, container_name):
    try:
        container = client.containers.get(container_name)
        container.remove()
        print(f"Conteneur '{container_name}' supprimé.")
    except Exception as e:
        print(f"Erreur lors de la suppression du conteneur : {e}")

# Fonction pour lister les conteneurs
def list_containers(client):
    containers = client.containers.list(all=True)
    if containers:
        print("Liste des conteneurs :")
        for container in containers:
            print(f"- {container.name} (ID: {container.id}, Status: {container.status})")
    else:
        print("Aucun conteneur trouvé.")

# Fonction principale
def main():
    # Affichage des options disponibles
    print("Veuillez choisir une action :")
    print("1 - Créer et démarrer un conteneur")
    print("2 - Arrêter un conteneur")
    print("3 - Supprimer un conteneur")
    print("4 - Lister les conteneurs")

    # Demander à l'utilisateur de choisir une action
    action = input("Entrez le numéro de l'action souhaitée (1/2/3/4) : ")

    # Paramètres par défaut
    image_name = "nginx"  # Image par défaut
    container_name = "mon_conteneur"  # Nom par défaut du conteneur
    ports = {"80/tcp": 8080}  # Exemple de mappage de port

    # Créer un client Docker
    client = get_docker_client()

    # Exécuter l'action choisie
    if action == "1":
        create_and_start_container(client, image_name, container_name, ports)
    elif action == "2":
        stop_container(client, container_name)
    elif action == "3":
        remove_container(client, container_name)
    elif action == "4":
        list_containers(client)
    else:
        print("Option invalide. Veuillez entrer un numéro valide (1/2/3/4).")
        sys.exit(1)

if __name__ == "__main__":
    main()
