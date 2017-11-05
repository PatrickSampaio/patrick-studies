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