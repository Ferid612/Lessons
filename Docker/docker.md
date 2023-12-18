## Docker

Portability. - Taşınabilir -lik.
Reproducibility. - Tekrarlanabilirlik.
Efficiency. - Randıman.
Scalability. - Ölçeklenebilirlik.  

![Alt text](image.png)


Docker Commands
There are “n” no.of commands in docker following are some of the commands mostly used.

Docker Run
Docker Pull
Docker PS
Docker Stop
Docker Start
Docker rm
Docker RMI
Docker Images
Docker exec
Docker Login

### Create Python File

!/main.py
print("Docker and GFG rock!")


### Create Docker File

FROM python:latest
COPY main.py /
CMD [ "python", "./main.py" ]




### Create docker image 
sudo docker build -t python-test .

### Əgər docker file adı fərqli isə 
### `sudo docker build -t python-test -f MyDockerfile .`
<br>

### `docker tag <image-id> <your dockerhub username>/python-test:latest`

### `docker push afrozchakure/python-test`


### Docker image e ait her şeyi silmek
###  docker rmi -f af939ee31fdc



docker run farid612/python-test
docker build farid612/python-test



