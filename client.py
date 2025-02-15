import ssl
from http.client import HTTPSConnection

HOST = "127.0.0.1"
PORT = 3300

#Criando contexto com SSL com o certificado gerado
context = ssl.create_default_context(cafile='certificate.pem')
print(context.get_ca_certs())

#Conexão
connection = HTTPSConnection('localhost', PORT, context = context)
connection.connect()

#REQUEST GET
connection.request('GET', '/')

#Receber a Resposta
resposta = connection.getresponse()
print(f"Mensagem da Resposta: {resposta.msg}\nStatus: {resposta.status}")
print(f"Resposta: {resposta.read().decode()}")

#POST REQUEST
texto = input("Texto para ser enviado no Post Request: ")
connection.request('POST', '/', texto)
#Receber a Resposta
resposta = connection.getresponse()
print(f"Mensagem da Resposta: {resposta}\nStatus: {resposta.status}")
print(f"Resposta: {resposta.read().decode()}")
connection.close()

#Encerrando a conexão
connection.close()
