from RedisClient import RedisClient
from Endpoint import Endpoint
from config import config

  
class Proxy:
  def __init__(self, redsmin_prod):
    #creating both sockets
    self.redisClient = RedisClient(config["uri"])
    self.endpoint = Endpoint(redsmin_prod)

    #binding data's transfer to the sockets
    self.redisClient.handle_read = self.sendDataFromRedisToEndPoint
    self.endpoint.handle_read = self.sendDataFromEndPointToRedis

    #calling the handshake
    self.endpoint.handshake()

  #transfer data from Redsmin to Redis (called when the sockets have something to read)
  def sendDataFromEndPointToRedis(self):
    data = self.endpoint.recv(8192)
    if(not self.endpoint.handshaken):
      print data
    self.redisClient.send(data)

  #transfer data from Redis to Redsmin (called when the sockets have something to read)
  def sendDataFromRedisToEndPoint(self):
    data = self.redisClient.recv(8192)
    self.endpoint.send(data)