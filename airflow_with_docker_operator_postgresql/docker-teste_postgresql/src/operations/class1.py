# classe

import os
from config import docker_env_variables

class DockerVariables:
    def my_function(self):  # Adicionando o argumento 'self'
        print("I'm running inside a docker Container, but outside of airflow schedule container")
        self.print_variables()  # Usando 'self' para chamar o método print_variables da mesma classe

    def print_variables(self):  # Adicionando 'self' como primeiro argumento
        print("Printing Docker variables:")
        print("DW_HOST:", docker_env_variables.get("DW_HOST"))
        print("DW_PORT:", docker_env_variables.get("DW_PORT"))
        print("DW_DATABASE:", docker_env_variables.get("DW_DATABASE"))
        print("DW_USER:", docker_env_variables.get("DW_USER"))
        print("DW_PASSWORD:", docker_env_variables.get("DW_PASSWORD"))
        print("MYSQL_GRAFANA_HOST:", docker_env_variables.get("MYSQL_GRAFANA_HOST"))
        print("MYSQL_GRAFANA_DB:", docker_env_variables.get("MYSQL_GRAFANA_DB"))
        print("MYSQL_GRAFANA_PORT:", docker_env_variables.get("MYSQL_GRAFANA_PORT"))
        print("MYSQL_GRAFANA_USER:", docker_env_variables.get("MYSQL_GRAFANA_USER"))
        print("MYSQL_GRAFANA_PASSWORD:", docker_env_variables.get("MYSQL_GRAFANA_PASSWORD"))

if __name__ == "__main__":
    docker_instance = DockerVariables()  # Criando uma instância da classe DockerVariables
    docker_instance.my_function()  # Chamando o método my_function a partir dessa instância

