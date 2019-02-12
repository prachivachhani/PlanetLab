import os

folderpath = "D:\\CCN\\Project2\\Final Submission\\Data Collection\\Pairwise Ping Data"

dirlist = os.listdir(folderpath)
for i in range(0, len(dirlist), 1):
    file1 = dirlist[i]

    openfilename = "PacketLoss of " + file1 +".csv"
    f = open(openfilename, 'w')

    with open(folderpath+"\\"+file1, 'r') as pingFile1:
        for line in pingFile1:
            try:
                if "20 packets transmitted" in line:
                    data = line.split(",")
                    temp = data[1]
                    values = temp.split(" ")
                    packetsRec = int(values[1])
                    packetsLoss = 20 - packetsRec
                    f.write(str(packetsLoss)+'\n')

            except Exception as e:
                print (e)
                pass
