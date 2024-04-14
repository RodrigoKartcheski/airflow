
Clonar o repositorio do GitHub
Fazer o Build do Docker: <docker build . --tag docker-operator-etl:1.0>
Iniciar o Docker compose do Airflow: <docker compose up>
Se falhar, abrir o terminar do HOST* e rodar para fins de teste o comando <sudo chmod 777 /var/run/docker.sock> (jamais em produção)
* no exemplo, host é o notebook ou PC que está sendo usando como servidor dos conteineres. Na prática, o host é um computador ligado à rede com domínio e IP fixos que fornece recursos e serviços para sites, blogs e aplicativos móveis.
