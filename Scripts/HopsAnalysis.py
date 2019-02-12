import os
import csv

folderpath = "D:\\CCN\\Project2\\Final Submission\\Data Collection\\Nodewise Trace Data"

for file in os.listdir(folderpath):
    filepath = folderpath+"\\"+file

    hopcount = 0
    inSameTrace = 0
    to =""

    with open(filepath, 'r') as pingFile:
        writein = "number_of_hops_in_" + file + ".csv"
        f = open(writein, 'w')
        f.write("Node To Reach, Number of hops\n")
        for line in pingFile:
            if line.startswith("traceroute"):
                inSameTrace = 1
                to = line.split(" ")[2]
                continue
            if (inSameTrace == 1 and len(line.strip()) != 0):
                hopcount += 1
            if (inSameTrace == 1 and len(line.strip()) == 0):
                print(to, " ", hopcount)
                f.write(to + "," + str(hopcount) + '\n')
                inSameTrace = 0
                hopcount = 0

