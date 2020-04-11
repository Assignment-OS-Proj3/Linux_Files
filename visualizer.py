import csv

ip_list = []

with open('log.csv', 'r') as csv_file:
    csv_reader = csv.reader(csv_file)

    next(csv_reader)
    
    for line in csv_reader:
        line_tuple = (line[0], line[1], line[2])
        ip_list.append(line_tuple)
