import asyncore, socket
from config import config
import json

class Endpoint(asyncore.dispatcher):
  def __init__(self, redsmin_prod):
    asyncore.dispatcher.__init__(self)
    self.create_socket(socket.AF_INET, socket.SOCK_STREAM)
    self.handshaken = False

    #can be used in developpement environment
    if(redsmin_prod):
      self.connect(('ssl.redsmin.com', 993))
    else:
      self.connect(('ssl.redsmin.dev', 993))

  #called when the socket is connected
  def handle_connect(self):
    print 'Endpoint connected'

  #called when the socket is closed
  def handle_close(self):
    self.close()
    print 'Endpoint closed'

  #Redsmin needs a handshake
  def handshake(self):
    self.send(json.dumps({'version':"1.1.0", 'key':config['key'],'auth':config['auth']}))