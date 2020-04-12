# Linux_Files

To run this, move the lkm.c and the Makefile to your home directory in Ubuntu.

Next, you will want to make sure that the storm containers are running. If the images havent been ran yet, see the following link to get the Storm UI running.
https://hub.docker.com/_/storm

Follow the steps to Set Up a Minimal Cluster, ignoring step number 4.

Once you've done this, you can confirm that the images are running by typing sudo docker ps.

You should have at least three images running. You can confirm the UI was setup correctly by visiting the localhost at port 8080.

Before running the LKM, make sure to clear the dmesg to avoid erroneous information in our output file

    ~$ sudo dmesg --clear

Type the following commands into the terminal to run the lkm:

    ~$ sudo make
    ~$ sudo insmod lkm.ko

What I did to get the output file was move the dmesg to a .csv file,  using the command

    ~$ dmesg > log.csv

Once the output file is created, we can remove the module off the kernel using `~$ sudo rmmod lkm.ko` and move on to show our communications using the visualizer tool.

The tool is written in python and requires python installed to be ran. In order to run it, make sure that the terminal is open at the 'log.csv' file's location. To run it, simply type:

    ~$ python visualizer.py

The tool will run and show the communications registered in our log. To exit the visualization simply click anywhere on the window.

