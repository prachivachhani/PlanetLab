import os

folderpath = "D:\\CCN\\Project2\\Final Submission\\Data Collection\\Pairwise Ping Data"

dirlist = os.listdir(folderpath)
for i in range(0, len(dirlist), 2):
    file1 = dirlist[i]
    file2 = dirlist[i+1]

    fromfile = file1.split("_")
    print(fromfile[2])
    tofile = file1.split("_")
    print(tofile[4])

    openfilename = "Latency of " + fromfile[2] + " and " + tofile[4] + ".csv"
    f = open(openfilename, 'w')

    with open(folderpath+"\\"+file1, 'r') as pingFile1:
        for line in pingFile1:
            try:
                if line.startswith("rtt min/avg/max/mdev"):
                    data = line.split("=")
                    values = data[1].split("/")
                    f.write(str(values[1]) + '\n')

            except Exception as e:
                print (e)
                pass

    with open(folderpath+"\\"+file2, 'r') as pingFile2:
        for line in pingFile2:
            try:
                if line.startswith("rtt min/avg/max/mdev"):
                    data = line.split("=")
                    values = data[1].split("/")
                    f.write(str(values[1]) + '\n')

            except Exception as e:
                print (e)
                pass
