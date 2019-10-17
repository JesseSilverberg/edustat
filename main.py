# from random import random
# import wget
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.firefox.options import Options
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

toRemove = []
with open('data/remove.csv') as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        toRemove.append([row[0], row[1]])

with open('data/rc_base.csv') as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        # Data cleaning
        if row[0] == "1819" and row[5] != '0000' and row[1] not in ['68', '71', '72', '73', '74', '75'] and row[
            5] not in ['8017', '2067', '9022'] and not (row[1] == '16' and row[5] == '0501') and not (
                row[1] == '53' and row[5] == '1661') and not (row[1] == '53' and row[5] == '1561') and not (
                row[1] == '50' and row[5] == '2791') and all(school != [row[1], row[5]] for school in toRemove):

            if row[21] == 'YES':
                # District ID, School ID, District Name, School Name, Lat, Long, Total students
                charters.append([row[1], row[5], row[3], row[6], row[17], row[18], row[37]])
            else:
                others.append([row[1], row[5], row[3], row[6], row[17], row[18], row[37]])

props = []
for i in range(1, 68):
    with open('data/' + str(i) + '.csv') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            if row[3] == "Students with Disabilities" and row[2] != '0000':
                for school in charters:
                    if school[1] == row[2] and school[0] == row[1]:
                        ###SWD count,
                        school.append(row[5])
                        props.append([school[0], school[1], float(school[7]) / float(school[6])])
                for school in others:
                    if school[1] == row[2] and school[0] == row[1]:
                        school.append(row[5])
                        props.append([school[0], school[1], float(school[7]) / float(school[6])])

                # print(row)
                # print(row[5])

print(charters)
print(others)
print("f")
print(props)
with open('props.csv', 'w') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(["District", "School", "prop"])
    for prop in props:
        if prop[2] > .999 and prop[2] > 0.69:
            print("and not (row[1] == '" + prop[0] + "' and row[5] == '" + prop[1] + "')", end=' ')
        writer.writerow(prop)
print()
for charter in charters:
    if len(charter) < 8:
        charters.pop(charters.index(charter))
clusters = copy.deepcopy(charters)
for cluster in clusters:
    cluster.append([])

# print(clusters)
# print(charters)
for school in others:
    min = charters[0]
    for charter in charters:
        if (float(school[4]) - float(charter[4])) ** 2 + (float(school[5]) - float(charter[5])) ** 2 < (
                float(school[4]) - float(min[4])) ** 2 + (float(school[5]) - float(min[5])) ** 2:
            min = charter
    # print(min)
    clusters[charters.index(min)][8].append(school)

print(clusters)

# Format is district id, school id, lat, long, total students, swd, [list of the publics in the same format]


with open('clusters.csv', 'w') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(["District Name", "School Name", "Lat", "Long", "Charter Count", "Other Count", "Charter Total", "Other Total"])
    for cluster in clusters:
        tot = 0
        count = 0
        for school in cluster[8]:
            # print(school)
            tot += int(school[6])
            count += int(school[7])
        # Lat, Long, Charter count, other count, charter total, other total
        if tot != 0:
            writer.writerow([cluster[2], cluster[3], cluster[4], cluster[5], cluster[7], count, cluster[6], tot])
