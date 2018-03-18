# Some Techniques to handler Docker Forest

## Running a host-like container

`docker exec -i -t docker_container_id /bin/bash`

- `-i` Allows CLI interaction with the proccess
- `-t` Indicates that you wan't to set up a TTY(?) to allow you to start a terminal
- `/bin/bash` Start terminal inside the container

## One service per Container

Currently one service by container is the architecture considered the best. There are some points regarding this architecture.
First of all, if you have separated services per container, you persist the single-responsibility principle, this makes your
ecosystem more flexible, each container have your responsability, and that unitary architecture, makes it easy to replace
or repeal something, but in I.T world, we don't have universal truths, so it's good to se the pros and cons to your case.
Besides the argument quoted above, there are some concrete aspects, building a DockerFile is faster when you have unit-like
containers.

### Example of a Monolithic

If you have an DB, APP and Web. When you have to build one, you are going to have to rebuild them all.

![alt text](https://github.com/PatrickSampaio/patrick-studies/blob/master/images/Screenshot%20from%202018-03-16%2009-44-40.png)

In the commands above, there is the use of the `copy` command, the usage of that commands allows the system to not create a new
DB every time that a script changes, the docker's cache is very simple, but the image will have to build, in every that that
is made on the scripts

### Example of unit-like containers

#### Database Dockerfile
`
FROM ubuntu:14.04
RUN apt-get update && apt-get install postgresql
WORKDIR /opt
COPY db /opt/db
RUN service postgresql start && \
cat db/schema.sql | psql && \
service postgresql stop
`

#### App Dockerfile
`
FROM ubuntu:14.04
RUN apt-get update && apt-get install nodejs npm
WORKDIR /opt
COPY app /opt/app
RUN cd app && npm install
RUN cd app && ./minify_static.sh
`

#### Web Dockerfile
`
FROM ubuntu:14.04
RUN apt-get update && apt-get install nginx
WORKDIR /opt
COPY conf /opt/conf
RUN cp conf/mysite /etc/nginx/sites-available/ && \
cd /etc/nginx/sites-enabled && \
ln -s ../sites-available/mysite
`

Developing in unit-like container allows you to only rebuild what you have changed. This is specially useful when you have
time-intesive setup on the configuration
There are some issues with that design as well. YOu have some duplication between images, and you have to make work
to link those container, `docker-compose` will help us

## Docker Commit

If you wanna to save the state of an container at a given moment, there is a command for doing that.

![alt text](https://github.com/PatrickSampaio/patrick-studies/blob/master/images/Screenshot%20from%202018-03-18%2017-29-16.png)

One thing, this command will save the filesystem state, not the proccess.

![alt text](https://github.com/PatrickSampaio/patrick-studies/blob/master/images/Screenshot%20from%202018-03-18%2017-30-25.png)

## Docker Tagging

Instead of using random ID's you can easily name an docker image using this technique

![alt text](https://github.com/PatrickSampaio/patrick-studies/blob/master/images/Screenshot%20from%202018-03-18%2017-40-29.png)

There are some concepts there are starting to get confuse

![alt text](https://github.com/PatrickSampaio/patrick-studies/blob/master/images/Screenshot%20from%202018-03-18%2017-40-38.png)

An image is just an layer above his parent image.
You can think about an Repository like an Git Repository, and when you clone the repository, you get the last image generated, an in the repository there are a lot of commit, each one it's going to be an image

Example of an multi image repository:

![alt text](https://github.com/PatrickSampaio/patrick-studies/blob/master/images/Screenshot%20from%202018-03-18%2017-45-14.png)

The latest means default in this context
