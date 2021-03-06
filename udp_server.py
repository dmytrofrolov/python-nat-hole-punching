import logging
import socket
import sys
from util import *
from connection import *
import time
import os

logger = logging.getLogger()
# addresses = []
connections = ConnectionsList()

def main(host='0.0.0.0', port=9999):
    sock = socket.socket(socket.AF_INET, # Internet
                         socket.SOCK_DGRAM) # UDP

    host = '0.0.0.0'
    port = os.environ.get('PORT', 6105)
    sock.bind((host, int(port)))
    while True:
        data, addr = sock.recvfrom(1024)

        logger.info("connection from: %s", addr)

        new_connection = Connection(addr, time.time())
        connections.addToList(new_connection)

        # sock.sendto(connections.getListJson(), addr)
        sock.sendto(new_connection.getJson(), addr)



if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(message)s')
    main(*addr_from_args(sys.argv))
