#!/bin/bash

git clone https://github.com/dmytrofrolov/python-nat-hole-punching.git

cd python-nat-hole-punching

echo "Starting server"

python3 udp_server.py 6105
