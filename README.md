# Linux_Files

To run this, move the lkm.c and the Makefile to your home directory in Ubuntu.

Next, you will want to make sure that the storm containers are running. If the images havent been ran yet, see the following link to get the Storm UI running.
https://hub.docker.com/_/storm

Follow the steps to Set Up a Minimal Cluster, ignoring step number 4.

Once you've done this, you can confirm that the images are running by typing sudo docker ps.

You should have at least three images running. You can confirm the UI was setup correctly by visiting the localhost at port 8080.

Type the following commands into the terminal to run the lkm:

    ~$ sudo make
    ~$ sudo insmod lkm.ko

To visualize the IPs, you can type `dmesg -t|tail` 

What I did to get the output file was move the tail to a .csv file, using the command

    ~$ dmesg -t|tail > log.csv

And I added the identifiers to each column of the table using the command

    ~$ sed -i 1i"Source IP Address, Destination IP Address, Package Count" log.csv
