Criar conexão entre 2 conteineres sendo 1 deles POSTGRESQL
criei o conteiner

baixei a imagem do postgres direto do hub
veio como postgres:13

rodei o comando abaixo:
docker run -d --name meu-postgres -p 5432:5432 -e POSTGRES_PASSWORD=postgres postgres:13

criei a rede:
docker network create minha-rede

Criei o conteiner operacional
docker build . --tag docker-ptg-teste:latest

docker run -d --name meu-docker-operator --network minha-rede docker-ptg-teste:latest

docker run -it --rm docker-ptg-teste:latest

obter o endereço IP do contêiner PostgreSQL. Você pode fazer isso executando o seguinte comando no host Docker:
docker inspect -f '{{range .NetworkSettings.Networks}}{{.IPAddress}}{{end}}' meu-postgres

#
ping 172.17.0.2

psql -h meu-postgres -U postgres -d postgres
psql -h 172.17.0.2 -U postgres -d postgres


#
cd /root/
python3 test_postgresql_connection.py
