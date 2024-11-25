# Implantação da Aplicação FastAPI no AWS EKS

Este tutorial mostra o processo de implantação de uma aplicação FastAPI integrada a um banco de dados PostgreSQL no Amazon Elastic Kubernetes Service (EKS). A aplicação utiliza o Kubernetes para orquestração, automatizando o deploy, o escalonamento e a gestão de workloads em contêineres. Ao final, a aplicação estará rodando na AWS, acessível através de um endpoint público.

## A aplicação está disponível em:
[App](http://ab4f4cec60b844f04afec87e03a9d22b-553677351.us-east-2.elb.amazonaws.com/docs#)

## Implantação pelo AWS CloudShell

## Passo 0: Baixar o Eksctl no CloudShell na versão UNIX

- Rode os comandos abaixo:
```bash
# for ARM systems, set ARCH to: `arm64`, `armv6` or `armv7`
ARCH=amd64
PLATFORM=$(uname -s)_$ARCH

curl -sLO "https://github.com/eksctl-io/eksctl/releases/latest/download/eksctl_$PLATFORM.tar.gz"

# (Optional) Verify checksum
curl -sL "https://github.com/eksctl-io/eksctl/releases/latest/download/eksctl_checksums.txt" | grep $PLATFORM | sha256sum --check

tar -xzf eksctl_$PLATFORM.tar.gz -C /tmp && rm eksctl_$PLATFORM.tar.gz

sudo mv /tmp/eksctl /usr/local/bin
```


## Passo 1: Criar o Cluster EKS

- Primeiro, crie um cluster EKS para hospedar sua aplicação e banco de dados.

```bash
eksctl create cluster --name projeto-cloud-cluster --region us-east-2 --nodes 2
```

- Explicação:

    - name: Nome do cluster (cloud-project-cluster).
    - region: Região AWS onde o cluster será criado (us-east-2, Ohio).
    - nodes: Quantidade de nós no cluster. Aqui utilizamos 2 nós para balancear a carga.

## Passo 2: Configurar o kubectl para Usar o Cluster EKS


- Atualize a configuração do Kubernetes local para apontar para o cluster EKS recém-criado:

```bash
aws eks --region us-east-2 update-kubeconfig --name projeto-cloud-cluster
```

- Explicação:

    - region: Região AWS onde o cluster foi criado.
    - update-kubeconfig: Atualiza a configuração do kubectl para conectar-se ao cluster EKS.
    - name: Nome do cluster. 


- Teste a conexão listando os nós do cluster:

```bash
kubectl get nodes
```

Você deve ver a lista de nós no cluster.

## Passo 3: Definir o Deployment da Aplicação
- Crie um arquivo de deployment (app-deployment.yml) para a aplicação FastAPI:

```bash
apiVersion: apps/v1
kind: Deployment
metadata:
  name: fastapi-app
spec:
  replicas: 1
  selector:
    matchLabels:
      app: fastapi
  template:
    metadata:
      labels:
        app: fastapi
    spec:
      containers:
        - name: fastapi
          image: davidconselvan/projeto-cloud:latest
          ports:
            - containerPort: 8000
          env:
            - name: DATABASE_URL
              value: "postgresql://projeto:projeto@postgres:5432/projeto"
---
apiVersion: v1
kind: Service
metadata:
  name: fastapi-service
spec:
  type: LoadBalancer
  ports:
    - port: 80
      targetPort: 8000
  selector:
    app: fastapi
```

- Explicação:

    - Deployment: Define como implantar a aplicação FastAPI como um pod.
    - Service: Expõe a aplicação usando um LoadBalancer, tornando-a acessível pela internet.


## Passo 4: Definir o Deployment do Banco de Dados
- Crie um arquivo de deployment (db-deployment.yml) para o banco de dados PostgreSQL:

```bash
apiVersion: apps/v1
kind: Deployment
metadata:
  name: postgres-db-cloud
spec:
  replicas: 1
  selector:
    matchLabels:
      app: postgres
  template:
    metadata:
      labels:
        app: postgres
    spec:
      containers:
        - name: postgres
          image: postgres:17
          ports:
            - containerPort: 5432
          env:
            - name: POSTGRES_USER
              value: "projeto"
            - name: POSTGRES_PASSWORD
              value: "projeto"
            - name: POSTGRES_DB
              value: "projeto"
---
apiVersion: v1
kind: Service
metadata:
  name: postgres
spec:
  ports:
    - port: 5432
  selector:
    app: postgres
```

- Explicação:

    - Deployment: Configura um pod para o banco de dados PostgreSQL.
    - Service: Expõe o banco de dados internamente dentro do cluster Kubernetes.

## Passo 5: Aplicar os Recursos no Cluster
- Aplique os arquivos de configuração no cluster Kubernetes:

```bash
kubectl apply -f app-deployment.yml
kubectl apply -f db-deployment.yml
```

- Explicação:

    - kubectl apply: Aplica as configurações YAML no cluster, criando os recursos definidos (pods, serviços, etc.).

### Verifique se os pods estão rodando:

```bash
kubectl get pods
```

## Passo 6: Acessar a Aplicação
- Depois que os serviços estiverem ativos, recupere o IP externo do serviço FastAPI:

```bash
kubectl get svc fastapi-service
```

- O comando retornará o EXTERNAL-IP do serviço. Use este IP para acessar sua aplicação em um navegador ou cliente de API.

