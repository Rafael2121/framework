# Framework

## Sobre o projeto

Este é um projeto de uma API REST que consulta um serviço externo e retorna
alguns desses resultados, porém somente o permitindo por meio de uma autenticação
por token.

Optei por utilizar o framework Django + Django Rest por 2 motivos: Por questões de 
experiência (não tem muito tempo desde que tive que atuar em um projeto django) e
para ter um utilitário que me fornecesse todas as ferramentas que eu precisaria. Mas é
possível ver que não é utilizado todo o ferramental do framework para o projeto.

O código está separado em bastante camadas, decidi fazer desta forma para separar bem
os componentes de baixo e alto nível, além de experimentar um pouco até onde o código
pode ir sem ser afetado pelo framework utilizado. Sendo assim é possível "enxutar" mais
o código para que ele ficasse concentrado em poucos arquivos, consequentemente menos 
complexo sem que virasse algo confuso.  

## Executando o projeto

O projeto utiliza o framework Django + Django REST então ele segue o padrão dos projetos
Django.

Atenção: o projeto usa como base a porta 8000, caso outro projeto esteja utilizando a 
mesma porta ele dará problema.

### Django manager

Case for executar na mão mesmo:


# Criar uma venv para não poluir sua área de trabalho
virtualenv .venv
source .venv/bin/activate 

# Instalar as dependencias
pip install -r requirements.txt

# Criar arquivo .env com variável com link do serviço
JSON_PLACEHOLDER_URL=https://jsonplaceholder.typicode.com

# Executar migrações
python manage.py migrate

# Executar projeto 
python manage.py runserver


### Docker-compose

Com com docker tudo fica mais simples, tudo será concentrado na criação da imagem +
composer


# na raiz do projeto

docker-compose build

docker-compose up


## Como utiliza-lo

O projeto em sí é bastante simples, ele consulta o serviço e retorna os 5 primeiros
elementos. Porém, para isso é necessário autenticar teu call.

Os endpoints disponíveis são:

POST http://127.0.0.1:8000/token-auth
body: {"username": "\<username>", "pass": "\<senha>"}

Como não é exatamente o foco do projeto, criei um endpoint bem simples que busca ou
cria um usuário e um token. Desta forma é bem rápido de o faze-lo.  

GET http://127.0.0.1:8000/

Realiza a busca no serviço, somente funciona quando enviado um 
"Authorization: Token \<token>" criado via POST. 

#### collection postman
Coloquei um arquivo com uma collection para executar os endpoints, assim fica bem mais
rápido de validar as coisas.

-> Framework-test.postman_collection.json