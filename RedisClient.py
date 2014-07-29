import asyncore, socket

class RedisClient(asyncore.dispatcher):
  def __init__(self, uri):
    asyncore.dispatcher.__init__(self)
    self.create_socket(socket.AF_INET, socket.SOCK_STREAM)

    #getting the port and hostname our of the uri
    self.port     = int(uri.split(':')[2])
    self.hostname = uri.split(':')[1][2:]

    #need a tuple with the hostname and the port
    self.connect((self.hostname, self.port))

  #called when the socket is connected
  def handle_connect(self):
    print 'Redis client connected'

  #called when the socket is closed
  def handle_close(self):
    self.close()
    print 'Redis client closed'