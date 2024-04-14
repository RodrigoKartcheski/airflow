#!task
from config import docker_env_variables


def mainer():
    print("I'm 3 running inside a docker Container, but outside of airflow schedule container")
    
    # Acessando as variáveis do arquivo config.py
    DW_HOST = docker_env_variables["DW_HOST"]
    DW_PORT = docker_env_variables["DW_PORT"]
    DW_DATABASE = docker_env_variables["DW_DATABASE"]
    DW_USER = docker_env_variables["DW_USER"]
    DW_PASSWORD = docker_env_variables["DW_PASSWORD"]
    MYSQL_GRAFANA_HOST = docker_env_variables["MYSQL_GRAFANA_HOST"]
    MSYQL_GRAFANA_DB = docker_env_variables["MSYQL_GRAFANA_DB"]
    MYSQL_GRAFANA_PORT = docker_env_variables["MYSQL_GRAFANA_PORT"]
    MYSQL_GRAFANA_USER = docker_env_variables["MYSQL_GRAFANA_USER"]
    MYSQL_GRAFANA_PASSWORD = docker_env_variables["MYSQL_GRAFANA_PASSWORD"]

    # Exemplo de uso
    print("DW_HOST:", DW_HOST)
    print("DW_PORT:", DW_PORT)
    print("DW_DATABASE:", DW_DATABASE)
    print("DW_USER:", DW_USER)
    print("DW_PASSWORD:", DW_PASSWORD)
    print("MYSQL_GRAFANA_HOST:", MYSQL_GRAFANA_HOST)
    print("MSYQL_GRAFANA_DB:", MSYQL_GRAFANA_DB)
    print("MYSQL_GRAFANA_PORT:", MYSQL_GRAFANA_PORT)
    print("MYSQL_GRAFANA_USER:", MYSQL_GRAFANA_USER)
    print("MYSQL_GRAFANA_PASSWORD:", MYSQL_GRAFANA_PASSWORD)

#if __name__=="__main__":
#    main()
