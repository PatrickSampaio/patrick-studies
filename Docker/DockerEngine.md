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


