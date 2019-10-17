#from random import random
#import wget
#from selenium import webdriver
# from selenium.webdriver.common.by import By
#from selenium.webdriver.firefox.options import Options
import csv
import copy

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

others = []
charters = []

with open('data/rc_base.csv') as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        if row[0] == "1819" and row[5] != '0000' and row[1] not in ['68', '71', '72', '73', '74', '75'] and row[
            5] not in ['8017', '2067', '9022'] and not (row[1] == '16' and row[5] == '0501') and not (
                row[1] == '53' and row[5] == '1661') and not (row[1] == '53' and row[5] == '1561') and not (
                row[1] == '50' and row[5] == '2791') and not (row[1] == '03' and row[5] == '0241') and not (row[1] == '03' and row[5] == '0281') and not (row[1] == '05' and row[5] == '0089') and not (row[1] == '05' and row[5] == '1028') and not (row[1] == '05' and row[5] == '1029') and not (row[1] == '06' and row[5] == '0871') and not (row[1] == '06' and row[5] == '1021') and not (row[1] == '06' and row[5] == '3222') and not (row[1] == '08' and row[5] == '0042') and not (row[1] == '13' and row[5] == '0921') and not (row[1] == '13' and row[5] == '1070') and not (row[1] == '13' and row[5] == '8151') and not (row[1] == '13' and row[5] == '8181') and not (row[1] == '16' and row[5] == '0281') and not (row[1] == '16' and row[5] == '1641') and not (row[1] == '16' and row[5] == '1701') and not (row[1] == '16' and row[5] == '2521') and not (row[1] == '17' and row[5] == '0922') and not (row[1] == '17' and row[5] == '0924') and not (row[1] == '20' and row[5] == '9106') and not (row[1] == '29' and row[5] == '0063') and not (row[1] == '29' and row[5] == '1202') and not (row[1] == '29' and row[5] == '2541') and not (row[1] == '29' and row[5] == '2972') and not (row[1] == '29' and row[5] == '3782') and not (row[1] == '29' and row[5] == '4002') and not (row[1] == '29' and row[5] == '4321') and not (row[1] == '29' and row[5] == '5371') and not (row[1] == '29' and row[5] == '6609') and not (row[1] == '29' and row[5] == '6639') and not (row[1] == '29' and row[5] == '7672') and not (row[1] == '31' and row[5] == '0131') and not (row[1] == '32' and row[5] == '0202') and not (row[1] == '35' and row[5] == '0533') and not (row[1] == '36' and row[5] == '0651') and not (row[1] == '36' and row[5] == '0701') and not (row[1] == '36' and row[5] == '9450') and not (row[1] == '37' and row[5] == '0452') and not (row[1] == '41' and row[5] == '2011') and not (row[1] == '42' and row[5] == '0471') and not (row[1] == '43' and row[5] == '0070') and not (row[1] == '46' and row[5] == '0241') and not (row[1] == '46' and row[5] == '0801') and not (row[1] == '48' and row[5] == '0011') and not (row[1] == '48' and row[5] == '0032') and not (row[1] == '48' and row[5] == '0055') and not (row[1] == '48' and row[5] == '0142') and not (row[1] == '48' and row[5] == '0177') and not (row[1] == '48' and row[5] == '0183') and not (row[1] == '48' and row[5] == '0591') and not (row[1] == '50' and row[5] == '2411') and not (row[1] == '50' and row[5] == '2521') and not (row[1] == '50' and row[5] == '3083') and not (row[1] == '50' and row[5] == '3391') and not (row[1] == '50' and row[5] == '3400') and not (row[1] == '50' and row[5] == '4100') and not (row[1] == '51' and row[5] == '4328') and not (row[1] == '52' and row[5] == '0681') and not (row[1] == '52' and row[5] == '1801') and not (row[1] == '52' and row[5] == '2581') and not (row[1] == '52' and row[5] == '3231') and not (row[1] == '53' and row[5] == '0092') and not (row[1] == '53' and row[5] == '0661') and not (row[1] == '53' and row[5] == '0962') and not (row[1] == '54' and row[5] == '0321') and not (row[1] == '55' and row[5] == '0061') and not (row[1] == '58' and row[5] == '0293') and not (row[1] == '59' and row[5] == '0281') and not (row[1] == '59' and row[5] == '0311') and not (row[1] == '64' and row[5] == '9850') and not (row[1] == '67' and row[5] == '0123'):

            if row[21] == 'YES':
                # District, School, Lat, Long, Total students
                charters.append([row[1], row[5], row[17], row[18], row[37]])
            else:
                others.append([row[1], row[5], row[17], row[18], row[37]])

props=[]
for i in range(1, 68):
    with open('data/' + str(i) + '.csv') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            if row[3] == "Students with Disabilities" and row[2] != '0000':
                for school in charters:
                    if school[1] == row[2] and school[0] == row[1]:
                        ###SWD count,
                        school.append(row[5])
                        props.append([school[0],school[1],float(school[5])/float(school[4])])
                for school in others:
                    if school[1] == row[2] and school[0] == row[1]:
                        school.append(row[5])
                        props.append([school[0],school[1],float(school[5])/float(school[4])])

                # print(row)
                # print(row[5])

print(charters)
print(others)
print("f")
print(props)
with open('props.csv', 'w') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(["District","School","prop"])
    for prop in props:
        if prop[2]>.999:
            print("and not (row[1] == '"+prop[0]+"' and row[5] == '"+prop[1]+"')",end=' ')
        writer.writerow(prop)
print()
for charter in charters:
    if len(charter) < 6:
        charters.pop(charters.index(charter))
clusters = copy.deepcopy(charters)
for cluster in clusters:
    cluster.append([])

# print(clusters)
# print(charters)
for school in others:
    min = charters[0]
    for charter in charters:
        if (float(school[2]) - float(charter[2])) ** 2 + (float(school[3]) - float(charter[3])) ** 2 < (
                float(school[2]) - float(min[2])) ** 2 + (float(school[3]) - float(min[3])) ** 2:
            min = charter
    # print(min)
    clusters[charters.index(min)][6].append(school)

print(clusters)

# Format is district id, school id, lat, long, total students, swd, [list of the publics in the same format]


with open('clusters.csv', 'w') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(["Lat", "Long", "Charter Count", "Other Count", "Charter Total", "Other Total"])
    for cluster in clusters:
        tot = 0
        count = 0
        for school in cluster[6]:
            # print(school)
            tot += int(school[4])
            count += int(school[5])
        # Lat, Long, Charter count, other count, charter total, other total
        if tot != 0:
            writer.writerow([cluster[2], cluster[3], cluster[5], count, cluster[4], tot])
