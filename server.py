import ssl
from http.server import HTTPServer, BaseHTTPRequestHandler
from io import BytesIO

HOST = '127.0.0.1'
PORT = 3300


#Implementação do GET e POST para lidar com requests HTTP no servidor 
class simpleHTTPRH(BaseHTTPRequestHandler):
    #lidando com requests GET
    def do_GET(self):
        #Response de 200, e de que tudo está OK
        self.send_response(200)
        self.end_headers()
        self.wfile.write(b'Servidor respondeu.')
    
    #lidando com POST request
    def do_POST(self):
        #Tamanho da mensagem
        len_mensagem = int(self.headers['Content-Length'])
        #ler o conteúdo da mensagem
        body = self.rfile.read(len_mensagem)
        #mandar resposta 200 para confirmar que está OK
        self.send_response(200)
        self.end_headers()
        resposta = BytesIO()
        resposta.write(b'Isso eh um POST request.\n')
        resposta.write(b'Mensagem recebida: ')
        resposta.write(body)
        self.wfile.write(resposta.getvalue())

#SSL/TLS
# chave e certificado gerados com o comando:
#openssl req -x509 -newkey rsa:2048 -keyout key.pem -out cert.pem -days 365
# comando para visualizar dados do certificado:
#openssl x509 -text -noout -in certificate.pem

#Protocolo SSL no socket para camada de segurança com certificado com a chave

context = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
context.load_cert_chain(certfile = 'certificate.pem', keyfile = 'key.pem')
context.check_hostname = False
print(f'Servidor rodando em localhost 127.0.0.1 , na port {PORT}')
httpd = HTTPServer((HOST, PORT), simpleHTTPRH)
httpd.socket = context.wrap_socket(httpd.socket, server_side = True) 
httpd.serve_forever() # não fecha a conexão do lado do servidor