# Sharing and Connecting docker images

That's an key point of docker, you can create an image, and share with other people, so the time that you lost making that
image, will not be lost again in another part of the wolrd, thus optmizing our time and moving our community forward.

## Docker Hub & Docker Registries

### Docker registries

First of all you must configure your machine to talk to docker hub

`docker run -d -p 5000:5000 -v $HOME/registry:/var/lib/registry registry:2`

- `/var/lib/{}` is where the registries files are going to be stored

### Docker Hub

Docker Hub is mantained by Docker Inc. It has thousands of images avaliable there, and it works like Github, but the difference
is that are images.

### Finding and running a Docker Image

`docker search {what_are_u_lookin_for}`

`docker search ubuntu`

![alt text](https://github.com/PatrickSampaio/patrick-studies/blob/master/images/Screenshot%20from%202018-03-11%2011-05-29.png)

Automated images are those built using Docker Hub’s automated build feature.

`docker run -t -i ubuntu-gpdb-dev`

- `-t` Creates an terminal for the container
- `-i` Specifies that the Docker Session is interactive
