# Logs Analysis Project

Building an informative summary logs from the database ( newspaper articles )

By answer three questions

1.What are the most popular three articles of all time?

2.Who are the most popular article authors of all time?

3.On which days did more than 1% of requests lead to errors?

## Run

1.Use the Git Bash terminal that comes with the Git software.

2.Install VirtualBox that actually runs the virtual machine.

3.Install Vagrant that configures the VM and lets you share files between your host computer and the VM's filesystem.

4.Download and unzip this file: FSND-Virtual-Machine.zip This will give you a directory called FSND-Virtual-Machine from here [FSND-Virtual-Machine](https://d17h27t6h515a5.cloudfront.net/topher/2017/August/59822701_fsnd-virtual-machine/fsnd-virtual-machine.zip).

5.From your terminal, inside the vagrant subdirectory, run the command vagrant up. This will cause Vagrant to download the Linux operating system and install it.

6.Run vagrant ssh to log in to your newly installed Linux VM!.

7. You will need to unzip this file newsdata.sql after downloading it, Put this file into the vagrant directory, which is shared with your virtual machine, download from here [newsdata.sql](https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip).

8.Inside the VM, change directory to /vagrant and look around with ls.

9.To load the data, use the command psql -d news -f newsdata.sql.

10.Finally run the script python project.py.

## some issues in running the program:

1."Timed out while waiting for the machine to boot" the virtualization settings in BIOS that were turned off and needed to be turned on.

2."file cant found" when changing directory to /vagrant. better to save adirectory FSND-Virtual-Machine in drive C:.

3."command not found" when use the command psql -d news -f newsdata.sql. run vagrant halt,destroy then re process vagrant up, ssh.

4."UserWarning: The psycopg2 wheel package will be renamed from release 2.8" amend some command in vagrantfile 

Change the box template to be "bento/ubuntu-16.04". No need of i386.

It is expected that vagrant mount the folder on "/vagrant" in the guest automatically. However, it does not work and the fix is to do that explicitly (synced_folder)

psycopg2 is renamed to psycopg2-binary. It should be considered with "apt-get install"

## Exit program

1.Run \q
2.Run command exit

## Program Version

Python 2.7