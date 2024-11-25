# Web Scraping com API REST: Docker e AWS

## Nome do Aluno

**Nome:** David Matheus Seixas Conselvan

---

## Overview do Projeto

Este projeto consiste em uma aplicação de scraping para extrair dados de fontes específicas da web e disponibilizá-los por meio de uma API RESTful, sem interface gráfica, construída utilizando FastAPI e PostgreSQL. A arquitetura é baseada em contêineres para garantir portabilidade e facilidade de execução, com as imagens hospedadas no Docker Hub.

A aplicação foi implantada na AWS utilizando o Elastic Kubernetes Service (EKS), uma ferramenta gerenciada para execução do Kubernetes. O Kubernetes automatiza a implantação, o dimensionamento e a gestão de aplicações em contêineres. No ambiente EKS, dois pods foram criados:

- Um para a aplicação FastAPI.
- Outro para o banco de dados PostgreSQL.

A comunicação entre os pods foi configurada para que a aplicação possa acessar o banco de dados e realizar as operações descritas. O uso do EKS garante escalabilidade, resiliência e gestão eficiente da aplicação em produção.

### A API oferece três endpoints principais:

- Registro de usuário: Permite criar novos usuários e devolve um token JWT para autenticação.
- Login: Permite que usuários registrados façam login e obtenham o mesmo token JWT.
- Consulta de dados externos: Acessa dados diários do mercado financeiro de uma API externa, exigindo autenticação com o token JWT.

---

## Repositórios  
- [Github](https://github.com/DavidConselvan/projeto-cloud)  
- [Docker Hub](https://hub.docker.com/repository/docker/davidconselvan/projeto-cloud/general)
---

### Documentação Aplicações:
[Aplicação Local](docker.md)
[Aplicação AWS](aws.md)