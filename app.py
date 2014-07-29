import sys, getopt, asyncore
from Proxy import Proxy

def main(argv):
  redsmin_prod = True

  #used to define the environment
  opts, args = getopt.getopt(argv,"d")
  for opt, arg in opts:
    if opt == '-d':
      redsmin_prod = False

  proxy = Proxy(redsmin_prod)
  
  #loop thought the sockets
  asyncore.loop()

if __name__ == "__main__":
  main(sys.argv[1:])