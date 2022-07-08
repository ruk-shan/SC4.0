# SC4.0_sim

## Instructions to run docker image
1. Download the repo <br>
2. Make sure you have installed <br>
  Docker,(https://docs.docker.com/engine/install/ubuntu/)<br> 
  Docker compose (https://www.digitalocean.com/community/tutorials/how-to-install-and-use-docker-compose-on-ubuntu-20-04) <br>
  (if you have a Nvidia GPU) nvidia docker tool kit (https://docs.nvidia.com/datacenter/cloud-native/container-toolkit/install-guide.html#docker) <br>
  if you don't have a Nvidia GPU, remove line 7 to 12 in docker compose file. <br>
3. Run the docker compose file "sudo docker-compose up -d" <br>
4. novnc > Browse http://127.0.0.1:6083/  (you can change the port numner in compose file) <br>
4. VNC > Browse 127.0.0.1:5900  (you can change the port numner in compose file) <br>
