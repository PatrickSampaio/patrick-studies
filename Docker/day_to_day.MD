## Day-2-Day Docker

### Docker Volume

It's possible to map an docker container folder to redirect to an host folder:

`docker run -v /var/db/1:/var/db debian`

In this command the folder `/var/db` of the container will have the content of the `var/db/1`
