TCP/UDP NAT Hole Punching
-------------------------

[Hole punching paper](http://www.brynosaurus.com/pub/net/p2pnat/)


# To build the server docker image
sudo docker build -t udp_echo_server_image .

 
# To run index server docker container
# In background:
sudo docker container run --rm -d --name udp_echo_server_container -e PORT=6105 -p 6105:6105/udp udp_echo_server_image

# Interactive:
sudo docker container run --rm -it --name udp_echo_server_container -p 6105:6105/udp udp_echo_server_image


# Stop container
sudo docker container stop udp_echo_server_container


# Save image to file
sudo docker save udp_echo_server_image -o udp_echo_server_image.tar

# Import image file to image
sudo docker load udp_echo_server_image.tar