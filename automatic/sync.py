import os

import csv

city = []

with open('/home/prince/automatic/city.csv','r') as csvFile:
    reader = csv.reader(csvFile)
    for row in reader:
        string = ""+row[2]
        string = string.replace(" ","")
        file_str = "sorted_"+row[0]+"_"+row[1]+"_"+row[3]+"_"+string
        city.append(file_str)

csvFile.close()

print(city)

for r in city:
    if(os.path.exists("/home/prince/automatic/"+r)):
        str = "/home/prince/automatic/"+r+"/*.csv > "+ "~/programs/project/goraahi/"+r+".csv"
        os.system("cat "+str)
        os.system("rm -r /home/prince/automatic/"+r)
