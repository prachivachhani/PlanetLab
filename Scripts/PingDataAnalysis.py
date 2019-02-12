import os

folderpath = "C:\\Users\\\prach\\Desktop\\Unix_Folder_On_Server\\Final Data\\Ping Data"

for file in os.listdir(folderpath):
    sumOfMax = 0.0
    sumOfMin = 0.0
    sumOfAvg = 0.0
    sumOfMdev = 0.0

    totalData = 0

    with open(folderpath+"\\"+file, 'r') as pingFile:
        print("File name: ", file)
        for line in pingFile:
            try:
                if "rtt min/avg/max/mdev" in line:
                    data = line.split("=")
                    values = data[1].split("/")

                    min = values[0]
                    avg = values[1]
                    max = values[2]
                    mdev = values[3].split("ms")[0]

                    sumOfMin += float(min)
                    sumOfAvg += float(avg)
                    sumOfMax += float(max)
                    sumOfMdev += float(mdev)

                    totalData += 1
            except Exception as e:
                print (e)
                pass

    fileMin = sumOfMin / totalData
    fileMax = sumOfMax / totalData
    fileAvg = sumOfAvg / totalData
    fileMdev = sumOfMdev / totalData

    print ("Max = ", float("%0.3f"%fileMax), "\tMin = ", float("%0.3f"%fileMin), "\tAvg = ", float("%0.3f"%fileAvg), "\tMdev = ", float("%0.3f"%fileMdev))
