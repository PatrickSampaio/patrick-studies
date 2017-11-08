#What is Hapenning on this machine?

W
-Time, Users, how many user are connected, load average
-Which users are connected

 09:36:01 up 1 day, 15:59,  1 user,  load average: 0,90, 0,71, 0,82
USER     TTY      FROM             LOGIN@   IDLE   JCPU   PCPU WHAT
geru     tty7     :0               Sex17   39:59m 56:46   0.63s /sbin/upstart -

TOP

	It's a command to show what proccess are running on the machine, and how much memory, process the are consuming

netstart -tupln

	Print network connections, routing tables, interface statistics, masquerade connections, and multicast memberships

Active Internet connections (w/o servers)
Proto Recv-Q Send-Q Local Address           Foreign Address         State      
tcp       32      0 192.168.1.119:32936     ec2-54-85-113-213:https CLOSE_WAIT 
tcp        0      0 localhost:34230         localhost:postgresql    ESTABLISHED
tcp        0      0 192.168.1.119:47554     gru06s29-in-f142.:https TIME_WAIT  
tcp        0      0 localhost:postgresql    localhost:34230         ESTABLISHED
tcp        0      0 192.168.1.119:36806     ec2-174-129-122-2:https ESTABLISHED
tcp        0      0 192.168.1.119:39332     ec2-52-206-150-24:https ESTABLISHED
tcp        0      0 192.168.1.119:58900     ec2-54-200-235-80:https ESTABLISHED
Active UNIX domain sockets (w/o servers)
Proto RefCnt Flags       Type       State         I-Node   Path
unix  2      [ ]         DGRAM                    685055   /run/wpa_supplicant/p2p-dev-wlp5s0
unix  20     [ ]         DGRAM                    14856    /run/systemd/journal/dev-log
unix  2      [ ]         DGRAM                    14860    /run/systemd/journal/syslog
unix  8      [ ]         DGRAM                    14867    /run/systemd/journal/socket
unix  6      [ ]         DGRAM                    26126    @nvidia2b5b87c2@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

