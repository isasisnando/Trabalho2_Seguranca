Código desenvolvido para o trabalho 2 da disciplina Segurança Computacional, no semestre 2024.2 na Universidade de Brasília.

# Trabalho de Implementação 2 – HTTPS

**Grupo:**

Elis Rodrigues Borges - 231018875

Isabela Souza Sisnando de Araujo - 231018884

Repositório do projeto no GitHub: https://github.com/isasisnando/Trabalho2_Seguranca

## Descrição

O objetivo deste projeto é implementar um sistema cliente-servidor que utiliza HTTPS com SSL/TLS, simulando uma comunicação segura entre as partes. Ele foi desenvolvido em Python, com o uso das bibliotecas **ssl** (para gerar e verificqar o certificado e a chave), **http** (para criar uma conexão HTTPS entre cliente e servidor, e realizar o tratamento de requisições) e **io** (para ler mensagens enviadas pelo terminal). Os arquivos são divididos da seguinte maneira:
- ```server.py```: código-fonte do servidor;
- ```client.py```: código-fonte do cliente;
- ```certificate.pem```: certificado SSL do servidor;
- ```key.pem```: chave SSL.

O certificado e a chave foram gerados executando o comando ```openssl req -x509 -newkey rsa:2048 -keyout key.pem -out cert.pem -days 365``` no terminal.


## Como executar

Tendo todos os arquivos baixados no mesmo diretório, siga os seguintes passos para conectar o cliente ao servidor utilizando HTTPS e simular uma comunicação segura:

1. Execute o ```server.py``` usando python.
2. Uma *pass phrase* será solicitada. Digite ```seguranca``` e aperte Enter.
3. O terminal deve, então, exibir a mensagem ```Servidor rodando em localhost 127.0.0.1 , na port 3300```. Essa foi a port escolhida porque ela não tem nenhuma funcionalidade própria, mas é comumente utilizada para serviços de comunicação, como é o caso deste projeto.
4. Enquanto o servidor estiver rodando, abra outro terminal e execute o ```client.py``` usando python.
5. O terminal do servidor deve, então, exibir a mensagem ```"GET / HTTP/1.1" 200 -```, antecedida pelo endereço de IP, data e hora da requisição, e o terminal do cliente deve exibir a mensagem ```Status: 200 Resposta: Servidor respondeu.```, juntamente de um prompt solicitando uma texto a ser enviado no Post Request. Digite a mensagem que quer enviar ao servidor e aperte Enter.
6. Se todo o processo tiver sido executado corretamente, o terminal do servidor vai exibir a mensagem ```"POST / HTTP/1.1" 200 -```, antecedida pelo endereço de IP, data e hora da requisição, e o terminal do cliente vai exibir a mensagem ```Status: 200 Resposta: Isso eh um POST request.``` e a mensagem recebida pelo servidor.
7. O cliente irá fechar a conexão e a execução do ```cliente.py``` será interrompida, mas o servidor continuará rodando. Para enviar uma nova mensagem, repita os passos de **4** a **6**.
