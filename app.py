import os
from flask import Flask
import socket         

app = Flask(__name__)
PORT1 = int(os.environ.get('PORT', 5000))

print("second app part running")
s = socket.socket()          
    
s.bind(('', PORT1))   
print ("Socket successfully created")
print ("socket binded to", PORT1)
print("HOSTNAME: ",socket.gethostname())  
print("Name HOSTNAME IP", socket.gethostbyname(socket.gethostname()))

# first of all import the socket library 

s.listen(5)      
print ("socket is listening")           
  
# a forever loop until we interrupt it or  
#  an error occurs 
while True: 
  
# Establish connection with client. 
 c, addr = s.accept()      
 print ('Got connection from', addr)
  
   # send a thank you message to the client.  
 c.send('Conection Completed Succefully'.encode() )
  
   # Close the connection with the client 
 c.close() 

print("first part app running")

@app.route('/')
def hello():
    print("hello running")
    return 'Sever Running!'

if __name__ == '__main__':
    # Bind to PORT if defined, otherwise default to 5000.
    print("if1 running")
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
    print("if running")

    



  







    
      
# print ("socket binded to %s", %(port) )
  

