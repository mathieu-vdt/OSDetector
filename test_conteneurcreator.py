import pytest
import docker
from conteneurcreator import create_and_start_container

# Test pour la création de conteneur sans utiliser unittest.mock
def test_create_and_start_container(mocker):
    # Utilisation de mocker pour simuler le client Docker et la méthode run
    mock_client = mocker.MagicMock()
    mock_run = mocker.MagicMock()
    
    # Simuler que la méthode 'containers.run' existe
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

