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
    # Vérifier les arguments
    if len(sys.argv) < 2:
        print("Usage: python conteneurcreator.py <action> [options]")
        sys.exit(1)

    action = sys.argv[1]
    image_name = "nginx"  # Image par défaut, vous pouvez changer cela en fonction de vos besoins
    container_name = "mon_conteneur"  # Nom par défaut du conteneur
    ports = {"80/tcp": 8080}  # Exemple de mappage de port

    # Créer un client Docker
    client = get_docker_client()

    if action == "create":
        # Créer et démarrer un conteneur
        create_and_start_container(client, image_name, container_name, ports)
    elif action == "stop":
        # Arrêter un conteneur
        stop_container(client, container_name)
    elif action == "remove":
        # Supprimer un conteneur
        remove_container(client, container_name)
    elif action == "list":
        # Lister les conteneurs
        list_containers(client)
    else:
        print(f"Action inconnue: {action}")
        sys.exit(1)

if __name__ == "__main__":
    main()
