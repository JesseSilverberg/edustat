from random import random

import wget
from selenium import webdriver
#from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options

"""
for i in range(1,10):

    print('Beginning file download with wget module'+str(i))

    url = 'https://edudata.fldoe.org/ReportCards/data/Enrollment/0'+str(i)+'.csv'
    wget.download(url, 'data/'+str(i)+".csv")


options = Options()
#options.headless = True
wd = webdriver.Firefox(options=options)
wd.set_page_load_timeout(30)
wd.get("https://edudata.fldoe.org/ReportCards/Schools.html?school=0021&district=04")

#https://edudata.fldoe.org/ReportCards/data/04.csv

print(wd.page_source)
#print(wd.find_element(By.ID, 'schooladdress'))
#print(wd.find_element_by_id('schooladdress').text)
print(wd.find_element_by_xpath('@swdDonut/tspan').text)

wd.close()
wd.quit()

"""

others=[]
charters=[]
import csv
import copy
numbers=[]
with open('data/rc_base.csv') as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        if row[0]=="1819" and row[5]!='0000' and row[1] not in ['68', '71', '72', '73', '74', '75' ] and row[5] not in ['8017','2067','9022'] and not (row[1]=='16' and row[5]=='0501') and not (row[1]=='53' and row[5]=='1661') and not (row[1]=='53' and row[5]=='1561'):
            if not row[1] in numbers:
                numbers.append(row[1])

            if row[21]=='YES':
                #District, School, Lat, Long, Total students
                charters.append([row[1],row[5],row[17],row[18],row[37]])
            else:
                if row[1]=='75':
                    print(row)
                others.append([row[1], row[5], row[17], row[18],row[37]])
for number in numbers:
    number=int(number)
numbers.sort()
print(numbers)
for i in range(1,68):
    with open('data/'+str(i)+'.csv') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            if row[3]=="Students with Disabilities" and row[2]!='0000':
                for school in charters:
                    if school[1]==row[2] and school[0]==row[1]:
                        ###SWD count,
                        school.append(row[5])
                for school in others:
                    if school[1]==row[2] and school[0]==row[1]:
                        school.append(row[5])

                #print(row)
                #print(row[5])

print(charters)
print(others)

for charter in charters:
    if len(charter)<6:
        charters.pop(charters.index(charter))
clusters=copy.deepcopy(charters)
for cluster in clusters:
    cluster.append([])

#print(clusters)
#print(charters)
for school in others:
    min=charters[0]
    for charter in charters:
        if (float(school[2])-float(charter[2]))**2+(float(school[3])-float(charter[3]))**2<(float(school[2])-float(min[2]))**2+(float(school[3])-float(min[3]))**2:
            min=charter
    #print(min)
    clusters[charters.index(min)][6].append(school)

print(clusters)

#Format is district id, school id, lat, long, total students, swd, [list of the publics in the same format]

with open('heatmap.csv', 'w') as csvfile:
    writer = csv.writer(csvfile)
    for cluster in clusters:
        writer.writerow([cluster[2],cluster[3],0.07*random()])


with open('clusters.csv', 'w') as csvfile:
    writer = csv.writer(csvfile)
    for cluster in clusters:
        tot=0
        count=0
        for school in cluster[6]:
            #print(school)
            tot+=int(school[4])
            count+=int(school[5])
        writer.writerow([cluster[2],cluster[3],cluster[5],count,cluster[4],tot])

