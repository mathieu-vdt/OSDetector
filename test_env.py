import pytest
import platform
import docker
from conteneurcreator import is_unix, get_docker_client, create_and_start_container

# Test pour la détection du système d'exploitation
def test_is_unix():
    # Vérifier si le système d'exploitation détecté est Unix (Linux ou macOS)
    if platform.system().lower() in ['linux', 'darwin']:
        assert is_unix() is True
    else:
        assert is_unix() is False

# Test pour vérifier que Docker est installé et fonctionne
def test_get_docker_client(mocker):
    # Utilisation de mocker pour simuler la présence de Docker
    mocker.patch('docker.from_env', return_value='docker_client')
    
    # Appel de la fonction pour obtenir le client Docker
    client = get_docker_client()
    
    # Vérifier si la fonction retourne le client Docker simulé
    assert client == 'docker_client'

# Test pour la création de conteneur (simuler la création du conteneur)
def test_create_and_start_container(mocker):
    # Créer un mock du client Docker
    mock_client = mocker.MagicMock()
    
    # Créer un mock pour la méthode 'containers.run'
    mock_run = mocker.MagicMock()
    mock_client.containers.run = mock_run
    
    # Paramètres pour la création du conteneur
    image_name = "nginx"
    container_name = "test_container"
    ports = {"80/tcp": 8080}

    # Simulation de la fonction
    result = create_and_start_container(mock_client, image_name, container_name, ports)

    # Vérifier si la méthode 'run' a été appelée avec les bons arguments
    mock_client.containers.run.assert_called_once_with(image_name, name=container_name, ports=ports, detach=True)

    # Vérifier que la fonction retourne bien le mock de 'run'
    assert result == mock_run.return_value
