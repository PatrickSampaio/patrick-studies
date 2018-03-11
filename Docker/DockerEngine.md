# Docker Engine

## Docker's architecture

![alt text](https://github.com/PatrickSampaio/patrick-studies/blob/master/images/Screenshot%20from%202018-03-09%2009-27-01.png)

## Docker daemon

Docker only runs where it can run his daemon. 

"Daemon is an process that runs in the background. A server is an process that responds to requests, an server in that only response to requests, is an example of an Daemon. The docker `command` is an client, and the Daemon is the server"

- Open your Docker daemon to the world

`to-do`

- Running containers as daemons

`to-do`

- Moving Docker to a different partition

`to-do`

## Docker Client

It's the simplest componenet in the docker architecture. It's job is bascially to send `HTTP` messages to the docker daemon.

### Problem
I want to debug a problem with a Docker command
### Solution
Using traffic snooper i can inspect docker daemon's api and craft my own apis
### Discussion

Use socat to monitor Docker API traffic

When a command is send to docker, those are the steps behind:

![alt text](https://github.com/PatrickSampaio/patrick-studies/blob/master/images/Screenshot%20from%202018-03-10%2010-54-44.png)

1 - The command is written in the terminal
2 - There is an HTTP request to an UNIX Domain Socket
3 - The UNIX domain socket calls the docker daemon

![alt text](https://github.com/PatrickSampaio/patrick-studies/blob/master/images/Screenshot%20from%202018-03-10%2011-04-18.png)

Try to run the command to see if it runs

Technique 5 - Use ports to connect to containers

`docker run -d -p 10002:80 --name blog2 tutum/wordpress`

-d tells to the container run as a daemon (? wtf)
-p tells that the port 10002 of the host will `hit` the port 80 of the docker container
-name name the docker container as blog2
And finally the image that the container is build upon is the tutum/wordpress

