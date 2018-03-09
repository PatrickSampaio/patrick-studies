## Docker

What is Docker?

Docker is a tool for creating sections inside your OS that contains other OS. Docker is more performatic then a virtualization tool because he uses resources from the native machine. Docker uses LXC services(Linux Containers)

## Container

A container is an isolated procces, that can start your applications in an isolated way.
Container is started by a procces on the host machine, and the container itself is going to have it's own proccess. A docker container is created based on an Docker Image. A container encapsulates the bin and libs required to execute an app

## Docker Image

Image is an model of files that are used to create a container. An image is create by an proccess called build or a command called commit. When you use an build, it will tell everything that you need to do to create that image. An image is composed by layers, each change that you make upon an image, it will create a layer in the original image. This architecture have a goal of reuse.

DockerHub is an repository of images

`sudo docker container run -p 8080:80 -v $(pwd):/usr/share/nginx/html nginx` 

You can run a container in an background proccess
`docker container run -d`

## Docker Container Commands

- `docker container ls/ps`	
- `docker container ls/ps -a`
- `docker container logs name`
- `docker container inspect name`
- `docker container uname name`

## Docker Image

- `docker image rm`
- `docker image inspect`
- `docker image tag`
- `docker image build`
- `docker image build -t ex-simple-build .`

## Docker layering

Multiple container from a same image share layers between then. What does this mean?

This means, for instance:

"I have an `docker image` that builds upon a `ubuntu image` and a `node image`, if i have more then 2 containers build from that image, it will share the `ubuntu` and `node` layer."

This can be done because of the static nature of those layers.









