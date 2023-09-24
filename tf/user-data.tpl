#!/bin/bash
sudo apt-get update
sudo apt-get install ca-certificates curl gnupg
sudo install -m 0755 -d /etc/apt/keyrings
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /etc/apt/keyrings/docker.gpg
sudo chmod a+r /etc/apt/keyrings/docker.gpg
echo \
  "deb [arch="$(dpkg --print-architecture)" signed-by=/etc/apt/keyrings/docker.gpg] https://download.docker.com/linux/ubuntu \
  "$(. /etc/os-release && echo "$VERSION_CODENAME")" stable" | \
  sudo tee /etc/apt/sources.list.d/docker.list > /dev/null
sudo apt-get update
sudo apt-get install -y docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin
<<<<<<< HEAD
#$tag = $ci_run_number
#echo $tag
sudo docker run -d -p 80:5000 --name flask shfarrukhb/flask:latest
=======
$tag = $ci_run_number
echo $tag
sudo docker run -d -p 80:5000 --name flask shfarrukhb/flask:$tag
>>>>>>> 6c5e33b202dfa3fa3abfccbb42dfcd5141a2608b
