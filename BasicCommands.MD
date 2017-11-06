#Linux Commands Line

###Directory

- `cd ~` it's a shortcut to your home
- pwd - Shows your current work directory
- `man {commnad}` - shows the manual of an command

- CTRL+R to search for last used commands
- ln -s file_to_link link_name <- It will create another pointer to the memory that the file_to_link points

- head file <- It will get the first 10 lines of file
- tail file <- Last 10 lines of the file
- tail file -f <- It will follown the file (*Changes in the file will be showed in the shell*)

- shutdown -h + 60 <- Schedule an turn off
- turnoff <- turn off the pc

- ls alh <- Give permission, size, created time and file name os the files
	
	total 20K
	drwxr-xr-x 3 geru admin 4,0K Nov  5 09:34 .
	drwxr-xr-x 9 geru admin 4,0K Nov  4 09:25 ..
    -rw-r--r-- 1 geru admin  581 Nov  5 09:19 BasicCommands.MD
    -rw-r--r-- 1 geru admin 1,9K Nov  5 09:42 MachineProccess.md
    -rw-r--r-- 1 geru admin    0 Nov  4 09:27 README.md

- Outputs

STDIN --> 0
STDOUT --> 1
STDERR --> 2

echo "string" 1> somefile.txt  <- Overrides an file named "somefile.txt" with the text "string"
ls -alh >> somefile.txt <- Append "String" to an file named somefile.txt

ls isajdijasdijasiji 2> err.txt  <- In case of the command is an error it will write into the file

- Pipes

`prog1 | prog2` <- Pipe will feed prog2 with the output of prog1

ps aux | less

The command `ps aux` give an return, pipe will hook up the return to the `less` command

- Fltering

CUT
`cat somefile.txt | cut -d: f2`
	Cut will look for the delimiter caracter `-d:` and will get the second group `f2`

SORT
`cat somefile.txt | sort -sortOptions`

Unique
`cat somefile.txt | uniq

GREP
`cat somefile.txt | grep "COMMAND"`
	Grep is an command to search patterns

##Permissions

d - owner
r - reader
w - write
x - execute

-rw-rw-r--

owner can read and write
users on the owner's group can read and write
everyone can read

7 - Can read write and execute
6 - Can read and write
4 - Can read
0 - Can do nothing

640 - Owner can read and write, the owner's group can read an everyone else can't do nothing

`chmod 740 somefile.txt`

`chown owner:group directory`

The command above changes the onwer's and owner'group of the file

##Groups and Users

`sudo -i`
`tail /etc/passwd`

usbmux:x:120:46:usbmux daemon,,,:/var/lib/usbmux:/bin/false

- first field is the username `usbmux`
- the x is in place of the password `x` 
- 120 is the user id `120`
- 46 is the default group id `46`
- humam readable information of the user `usbmux daemon ,,,`
- home directory `/var/lib/usbmux`
- the default shell `/bin/false`

`tail etc/shadow`

usbmux:*:17379:0:99999:7:::

- `usbmux` is the username
- `*` is the user password hashed, if the passwords is a `!`, you can't loggin with this user
- `17379` date that this password was set
- `0` :
- `99999` : date that the password expires
- `7` : how many days i can have to change the password

`tail etc/group`

plugdev:x:46:

- `plugdev` is the name of the group
- `46` is the id of the group

Commands:

- `useradd -m -d /home/testuser -u 1501 -g 66 -s`
	m - options is for create an home for that user
	d - options is for the home directory
	u - is for user id
	g - is for user's group id
	s - is the shell directory, if empty, it's the default
	username

	`passwd user` <- this command will give this user and passwd

- `userdell user`

Proccess

	If something is being done on linux, there is an proccess attached to it and a address. Kernel keeps track of data about the proccess, like who owns it, how much it consumes in terms of memory and etc.
	Every proccess has an ID. You can se which information Kernel has about the proccess by typing `top` on shell

		`proccess init has an ID 1, he is the fater of all proccess`

	A proccess owned by a user, not necessarily will have the owner permission
	Niceness <- remember Aires
	When an proccess is misbehaving the parent proccess is notified
	When a proccess dies the parent proccess is notified	
