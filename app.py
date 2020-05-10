import os
from flask import Flask
import socket         

app = Flask(__name__)




print("first part app running")

if __name__ == '__main__':
    # Bind to PORT if defined, otherwise default to 5000.
    print("if1 running")
    port = int(os.environ.get('PORT', 5000))


    print("second app part running")
    s = socket.socket()          
    
    s.bind(('', port))   
    print ("Socket successfully created")
   # first of all import the socket library 
       
  
    # next create a socket object 

  
  # reserve a port on your computer in our 
   # case it is 12345 but it can be anything 
  
 # Next bind to the port 
   # we have not typed any ip in the ip field 
 # instead we have inputted an empty string 
 # this makes the server listen to requests  
 # coming from other computers on the network 

 # put the socket into listening mode 
   s.listen(5)      
   print ("socket is listening")           
  
 # a forever loop until we interrupt it or  
 # an error occurs 
   while True: 
  
   # Establish connection with client. 
     c, addr = s.accept()      
     print ('Got connection from', addr)
  
   # send a thank you message to the client.  
     c.send('Thank you for connecting') 
  
   # Close the connection with the client 
     c.close() 



    app.run(host='0.0.0.0', port=port)
    print("if running")






@app.route('/')
def hello():
    print("hello running")
    return 'Sever Running!'


    
      
# print ("socket binded to %s", %(port) )
  

