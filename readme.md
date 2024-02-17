### API

![API CLIENT AND SERVER](/src/images/api.png)
- Temos o<bold>cliente</bold>que utiliza a <bold>internet</bold>para conseguir se conectar com o<bold>Servidor</bold>
- Comunicação feita através do HTTP- Comunicação integrada para que sempre que o cliente fizer uma solicitação, ele ira buscar
uma resposta para esse pedido, então ele entrega a informação.

- HTTP (HYPER TEXT TRANSFER PROTOCOL)
  - Este protocolo projetado para enviar conteúdo para internet, como HTML, vídeos, imagens e etc.
  ![CLIENT PROXY](/src/images/proxy.png)

  - Proxy são entidades que nos ajudam a fazer a comunicação, podem exercer diversas funções, digamos
  que o proxy é um representante, ele nós ajuda a operar as camadas de comunicação entre o pedido e a resposta.
  - Proxy - cacheamento se é publico ou privado.
  - cache é importante para performance.
  - Balanceamento de carga - através de um proxy - dimensionamento geografico para encaminhar para o servidor mais próximo da sua localidade para diminuir o tempo de espera e reduzir os custos.
  - proxy de autenticação e validação.
  - Cliente (Client)
  - Garçom (pedidos, levar seus pedidos, para a cozinha) (API)
  - Cozinha (Server)

  ### MÉTODOS DE REQUISIÇÃO HTTP
  - GET -> faz uma consulta a um registro ou uma coleção de registros do servidor.
    - Exemplo: estamos em um site pesquisando uma cadeira gamer de uma determinada marca, ele leva uma requisição do banco de dados da loja virtual, para trazer um resultado específico de uma cadeira ou uma coleção.
  - POST -> Envia dados para criar um 'um novo registro' no servidor
    - Exemplo: Posso registrar uma cadeira, ou várias cadeiras de uma única vez. Faz a inclusão do produto.
  - PUT -> Envia dados para atualizar um 'registro existente' no servidor.
    - Exemplo: Atualiza a lista de cadeira que esta com o preço errado.
  - DELETE -> Excluir registros do servidor.
    - Exemplo: Exclui um ou mais registros
  - PATCH -> Envia dados para atualizar parcialmente um registro existente no servidor.
    ### 4 principais elementos
    - CONNECT -> É usado para abrir uma conexão com o servidor remoto.Onde eu vou conseguir acessar? endpoint
    - OPTIONS -> É usado para descrever as opções de comunicação para um recurso específico.Uma chave de autenticação
    - TRACE -> foi projetado para fins de diagnostico durante o desenvolvimento. Ajuda a projetar um sistema de monitoramento
    - HEAD -> Recupera os cabeçalhos recursos - Cabeçalho da requisição que nos retorna informações e também os códigos de retorno.

### HTTP STATUS
    - Protocolo HTTPS.
      - STATUS CODE vem no head
        - 301 - Moved permanently
        - 200 - ok
        - 404 - not found

### HTTPS: HyperText Transfer Protocol Secure
![http](/src/images/http.gif)

![http x https](/src/images/http_x_https.png)
- HTTPS É uma extensão do HTTP, Adiciona o S de segurança
 - HTTP Não tem o serviço de encrypting não esta criando uma camada de segurança.
 - HTTPS Transforma a senha e garantir que o usuários que faz um acesso, faz um procedimento, como compra dentro de um e-commerce, tenha o seus dados seguros.Insere uma camada de proteção de dados entre o cliente e o servidor.
    - Condição criptografada para dados sensíveis.
      - CRIPTOGRAFIA -> Lingua única entre o servidor e um site
      - CERTIFICADO SSL

### INTRODUÇÃO A APIS
  APIs são interfaces que permitem a comunicação a integração entre diferentes aplicações de software(SITES, Aplicativos e dispositivos)

API = Application Programming interface / interface de Programação a aplicativos.
![API](/src/images/api.gif)
  - Conjunto de rotinas e padrões que nos fornecem acesso aos dados.
  - FORMATO REST - como um cartão postal, mais leve, pode ser armazenado em cache e mais fácil de atualizar,
  - FORMATO SOAP - é como um envelope. SObrecarga extra, mais largura de  banda necessária, mais trabalho em ambas as extremidades.

![CRUD](/src/images/crud.png)

### REST API
  - Representational State Transfer
![REST](/src/images/restapi_model.png)
![REST IN ACTION](/src/images/rest_in_action.png)

  - Principais elementos dessa arquitetura
            REST Clients                    REST REQUEST                        REST SERVER
    -Smartphone, desktop, IOT          GET/POST/PUT/DELETE METHOD                RESOURCE
                                                                                 RESOURCE
      XML/JSON/FORMAT                       REST RESPONSE                        RESOURCE

    - Esse método de solicitação de pedido é feito traves de um <bold>end-point/uri</bold>

        - Endpoint uri destino
        - headers - ele vai ter mais informações com o cliente, nesse cabeçalho que eu envio uma chave de autenticação.
        - body é onde utilizamos para conseguir transmitir essas informações adicionais ao nosso servidor e também é através do body que vamos receber a resposta para obter o conteúdo.
        - response - resposta negativa ou positiva. A resposta que vamos receber do servidor ela vai ser no formato xlm
    - Arquitetura REST API
    ![Arq rest api](/src/images/arquitetura_rest.png)


### FLASK WEB DEVELOPMENT ONE DROP AT TIME
- Flask é um micro framework que utiliza a linguagem python para criar aplicativos web.
- 1-sistema padronizado de gateway WSGI padrão de desenvolvimento em python para garantir conexão e a comunicação
- BASE Werkzeug nos ajuda de forma nativa no flask a implementar as requests, carregamento de dados, conexões, rotas de acesso, para nos ajudar a desenvolver o fluxo de comunicação
- Jinja componentização de templates web

### INSTALANDO O FLASK
- Comando
`$ mkdir myproject`
`$ cd myproject`
`$ python3 -m venv .venv`
`$ . .venv/bin/activate`
`$ pip install Flask`

### executando um projeto com o Flask
`flask --app app run`

- URL lib ajuda a manipular requisições para um endpoint.
- Json irá tratar os dados que recebi.

### FAST API

#### Características do Fast API
- Utilização Uvicorn e Starlette
  - Starlette => gestão de comunicação em tempo real
  - Uvicorn => Trabalha com a gestão a ambientes de servidores web, pensando no quesito performance.Interface padrão de servidores. ASGI
- Validação de tipos de dados com Pydantic
- Desempenho com resursos assíncronos
- escalabilidade
- Facilidade de uso.
- Documentação automática.

Síncrono x Assíncrono

![Sincrono x Assincrono](/src/images/sincrono_x_assincrono.png)

Serverless é o tipo de arquitetura onde vamos desenvolver apis que vao disparar funções de atividades com base em eventos.
- biblioteca assycIo