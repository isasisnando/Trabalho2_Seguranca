import ssl
from http.client import HTTPSConnection

PORT = 3300

#Criando contexto com SSL com o certificado gerado
context = ssl.create_default_context(cafile='certificate.pem')

#Caso deseje printar as informações do certificado, descomentar a linha de código abaixo
#print(context.get_ca_certs())

#Conexão
connection = HTTPSConnection('localhost', PORT, context = context)
connection.connect()

#REQUEST GET
connection.request('GET', '/')

#Receber a Resposta
resposta = connection.getresponse()
print(f"Status: {resposta.status}")
print(f"Resposta: {resposta.read().decode()}")

#POST REQUEST
texto = input("Texto para ser enviado no Post Request: ")
connection.request('POST', '/', texto)
#Receber a Resposta
resposta = connection.getresponse()
print(f"Status: {resposta.status}")
print(f"Resposta: {resposta.read().decode()}")

#Encerrando a conexão
connection.close()
