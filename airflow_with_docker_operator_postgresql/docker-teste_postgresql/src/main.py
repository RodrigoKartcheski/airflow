# Importe as funções dos seus arquivos

from config import docker_env_variables
from operations.task1 import mainer
from operations.class1 import DockerVariables


def main():
    print(f"iniciando processoamento - MONITORAMENTO_GRAFANA")
    data = mainer()
	    
    # Criar uma instância de DockerVariables
    docker_vars = DockerVariables()
    
    # Chamar o método my_function a partir da instância
    docker_vars.my_function()

    # Faça algo com os dados processados, se necessário

if __name__ == "__main__":
    main()
