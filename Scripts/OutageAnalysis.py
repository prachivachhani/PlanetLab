import os
import csv

folderpath = "D:\\CCN\\Project2\\Final Submission\\Data Collection\\Nodewise Trace Data"

fp = open("Outage Analysis.csv", 'a')
fp.write("Node Name, Permenent Failure, Temporary Failure, Total Failure\n")

for file in os.listdir(folderpath):
    filepath = folderpath+"\\"+file

    hopcount = 0
    inSameTrace = 0
    to = ""
    goDest = 0
    reachedDest = 0
    successReach = 0
    failureReach = 0

    matching = "*"
    tracesWithoutStar = 0
    totalTraces = 0


    with open(filepath, 'r') as pingFile:

        writein = "number_of_hops_in_" + file + ".csv"
        f = open(writein, 'w')
        f.write("Node To Reach, Number of hops\n")
        for line in pingFile:
            if line.startswith("traceroute"):
                inSameTrace = 1
                to = line.split(" ")[2]
                goDest = 1
                continue
            if (inSameTrace == 1 and len(line.strip()) != 0):
                hopcount += 1
                tracesWithoutStar += 1
                totalTraces += 1
                if to in line:
                    reachedDest = 1
                if matching in line:
                    tracesWithoutStar -= 1
            if (inSameTrace == 1 and len(line.strip()) == 0):
                print(to, " ", hopcount)
                f.write(to + "," + str(hopcount) + '\n')
                inSameTrace = 0
                hopcount = 0
                if goDest == reachedDest:
                    successReach += 1
                    goDest = 0
                    reachedDest = 0
                else:
                    failureReach += 1


    successPercentage = (tracesWithoutStar/totalTraces)*100
    failurePercentage = 100 - successPercentage

    print ("FOR NODE : ", file,  "\tNo. of successes: ", successReach, "\t No. of failures: ", failureReach)
    totalReach = successReach + failureReach
    PermFailurePercentage = (failureReach/totalReach)*100

    fp.write(file + ',' + str(PermFailurePercentage) + '%,' + "100%"+ ',' + str(failurePercentage) + '%\n')
