import csv
import random as r
import turtle as t

#Dictionary for IPs
ip_dict = {}
#Set keeps track of all the ips, no duplicates
ip_set = set()
#dictionary to keep track of the randomized coordinates of each ip (used later to draw the package comm.)
ip_screen = {}
#Initialize the turtle screen with size of 400x300 pixels
screen = t.Screen()
screen.screensize(400,300)

#Reads from CSV files
with open('log.csv', 'r') as csv_file:
    csv_reader = csv.reader(csv_file)

    next(csv_reader)
    #insert the contents of the CSV into the dictionary
    for line in csv_reader:
        #Checks if the IP is already in the set of IPs and adds it if not. Also checks for the destination IP
        if line[0] not in ip_set:
            ip_set.add(line[0])
        if line[1] not in ip_set:
            ip_set.add(line[1])
        #Checks that the src IP is not in the IP dictionary and maps it accordingly
        if line[0] not in ip_dict:
            ip_dict[line[0]] = []
            ip_dict[line[0]].append(line[1])
            ip_dict[line[0]].append(line[2])
        else:
            if ip_dict[line[0]][0] == line[1]:
                ip_dict[line[0]][1] = line[2]

    #Draw each "circle" for each IP
    for item in ip_set:
        #print(key + " goes to" + ip_dict[key][0] + " and exchanged " +
        #     ip_dict[key][1] + " packages")
        
        #Randomize x and y coordinates of the circle and store them in the screen dictionary
        rand_x = r.randrange(-350,350,1)
        rand_y = r.randrange(-300,300,1)
        ip_screen[item] = (rand_x, rand_y)
        #Sets the turtle color to red and its shape to a circle of size 2
        t.color("red")
        t.shape("circle")
        t.shapesize(1.5)
        #Lifts the "pen" so no line is drawn when moving the turtle
        t.penup()
        #Move the turtle to the randomized coordinates and stamp (paint the circle)
        t.setpos(rand_x, rand_y)
        t.stamp()
        #Stamps the IP with its respective circle
        t.setpos(rand_x, rand_y + 20)
        t.write(item, font=("Arial", 15, "bold"))

        
    #print(ip_screen)
    #Recreates a smaller turtle to show the communication between IPs
    t.shapesize(0.20)
    t.color("blue")
    t.shape("square")
    
    for key in ip_dict:
        #Hide the turtle while moving to a new location and increase the speed to move faster
        t.speed(10)
        t.hideturtle()
        t.penup()
        #The new position will be given by the randomized values stored in the screen dictionary, mapped to the IP (key)
        t.setpos(ip_screen[key][0], ip_screen[key][1])
        t.showturtle()
        t.speed(1.20)
        #Pen down to draw the line
        t.pendown()
        #New position is the destination source of the current key. Accessed via the IP dictionary, and reused by the
        #screen dictionary to find its coordinates.
        t.setpos(ip_screen[ip_dict[key][0]][0], ip_screen[ip_dict[key][0]][1])
        t.stamp()
        t.write(ip_dict[key][1], font=("Arial", 10, "bold"))
        t.speed(5)

    t.penup()
    t.hideturtle()
    t.setpos(0,0)
