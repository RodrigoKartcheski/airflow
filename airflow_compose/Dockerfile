FROM apache/airflow:2.5.1


USER root

# Instale as dependências necessárias
RUN apt-get update && apt-get install -y \
    curl \
    apt-transport-https \
    gnupg \
 && rm -rf /var/lib/apt/lists/*

# Adicione a chave de assinatura do repositório da Microsoft
RUN curl https://packages.microsoft.com/keys/microsoft.asc | tee /etc/apt/trusted.gpg.d/microsoft.asc

# Adicione o repositório do SQL Server à lista de fontes
RUN curl https://packages.microsoft.com/config/debian/11/prod.list | tee /etc/apt/sources.list.d/mssql-release.list

# Atualize os repositórios e instale o driver ODBC do SQL Server
RUN apt-get update && ACCEPT_EULA=Y apt-get install -y \
    msodbcsql17 \
    unixodbc-dev \
 && rm -rf /var/lib/apt/lists/*

# Instale as ferramentas do SQL Server (opcional)
RUN apt-get update && ACCEPT_EULA=Y apt-get install -y \
    mssql-tools \
 && rm -rf /var/lib/apt/lists/*

# Adicione o diretório das ferramentas do SQL Server ao PATH
RUN echo 'export PATH="$PATH:/opt/mssql-tools/bin"' >> ~/.bashrc \
 && /bin/bash -c "source ~/.bashrc"

# Instale a biblioteca Kerberos (opcional)
RUN apt-get update && apt-get install -y \
    libgssapi-krb5-2 \
 && rm -rf /var/lib/apt/lists/*
 
# Execute o comando ls de forma recursiva para listar todas as pastas e subpastas
RUN ls -lR / > /lista_pasta.txt


# Exiba o conteúdo do arquivo lista_pasta.txt
#RUN cat /tmp/lista_pasta.txt

COPY /dags ./dags
COPY requirements.txt requirements.txt

#USER root

# Adicionar o usuário 'airflow' ao grupo Docker e modificar as permissões do socket Docker
#RUN usermod -aG docker airflow && \
#    sudo chmod 777 /var/run/docker.sock


    
USER airflow


RUN pip install -r requirements.txt
########################################
#RUN sudo chmod +x /var/run/docker.sock
#RUN sudo usermod -aG docker $airflow

CMD ["/bin/bash"]


