
	
import SimpleHTTPServer
import SocketServer
 



PORT = 8201

print "Programa Inicializado"


class my_handler(SimpleHTTPServer.SimpleHTTPRequestHandler):
   def do_GET(self):
      self.send_response(200)
      self.send_header('Content-type','text/html')
      self.end_headers()
      self.wfile.write("<center><h1>Servidor em manutencao!</h1></center>")
      return
 
 
try:
   httpd = SocketServer.ThreadingTCPServer(('', PORT), my_handler)
 
   print "servidor web rodando na porta ", PORT
   httpd.serve_forever()
 
except KeyboardInterrupt:
   print "Voce pressionou ^C, encerrando..."
   httpd.socket.close()