
import os
import platform
import traceback
import datetime
import sys
import subprocess
import re
import itertools
import time

def pingServers():

    plat = platform.system()
    scriptDir = sys.path[0]
    hosts = os.path.join(scriptDir, 'MyNodes.txt')
    hostsFile = open(hosts, "r")
    lines = hostsFile.readlines()
    
    lines = map(lambda s: s.strip(), lines)
        
    for i in lines:
	for j in lines:
            if i!=j:    
	        try:
            	    j = j.strip()
            	    if plat == "Windows":
                        args = "ping -n 4 -w 10000 " + j
                    if plat == "Linux":
                        args = "ping -c 20 "+ j

	            server_name = "albany_ccn6@" + i
	            ssh_args = ["ssh", "%s" % server_name, args]
    		    print ssh_args
                    	
	            out = subprocess.Popen(ssh_args, shell=False, stdout = subprocess.PIPE, stderr = subprocess.PIPE)
                    results = out.stdout.readlines()
                    if results == []:
                        error = out.stderr.readlines()
                        print error 
                    else:
                        #print "\n", results
			results = map(lambda s: s.strip(), results)
		        for k in results:
				print k
                        filename = "PingData_From_" + i +"_To_" + j + ".txt"
                        f = open(filename, 'a')
                        for k in results:
							f.write(k)
							f.write("\n")
							f.close()
                except:
                    print "Error processing line: ", j
                    print "Error message: ", traceback.format_exc()

    hostsFile.close()
    print "------------ Process going in sleep -----------------"
    time.sleep(60*60)

while 1:
    pingServers()
