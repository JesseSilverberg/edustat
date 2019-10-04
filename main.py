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
with open('data/rc_base.csv') as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        if row[0]=="1819" and row[5]!='0000':
            if row[21]=='YES':
                #District, School, Lat, Long
                charters.append([row[1],row[5],row[17],row[18]])
            else:
                others.append([row[1], row[5], row[17], row[18]])

for i in range(1,68):
    with open('data/'+str(i)+'.csv') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            if row[3]=="Students with Disabilities" and row[2]!='0000':
                for school in charters:
                    if school[1]==row[2] and school[0]==row[1]:
                        school.append(row[5])
                for school in others:
                    if school[1]==row[2] and school[0]==row[1]:
                        school.append(row[5])

                #print(row)
                #print(row[5])

print(charters)
print(others)
clusters=copy.deepcopy(charters)
for cluster in clusters:
    cluster.append([])

print(clusters)
print(charters)
for school in others:
    min=charters[0]
    for charter in charters:
        if (float(school[2])-float(charter[2]))**2+(float(school[3])-float(charter[3]))**2<(float(school[2])-float(min[2]))**2+(float(school[3])-float(min[3]))**2:
            min=charter
    print(min)
    clusters[charters.index(min)][5].append(min)

print(clusters)