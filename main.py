# from random import random
# import wget
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.firefox.options import Options
import csv
import copy

"""
for i in range(10,68):

    print('Beginning file download with wget module'+str(i))
    url = 'https://edudata.fldoe.org/ReportCards/data/Achievement/' + str(i) + '.csv'
    #url = 'https://edudata.fldoe.org/ReportCards/data/Enrollment/0'+str(i)+'.csv'
    wget.download(url, 'data/Achievement/'+str(i)+".csv")


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
    next(reader)
    for row in reader:
        toRemove.append([int(row[0]), int(row[1])])

with open('data/rc_base.csv') as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        # Data cleaning
        if row[0] == "1819" and row[5] != '0000' and row[1] not in ['68', '71', '72', '73', '74', '75'] and row[
            5] not in ['8017', '2067', '9022'] and not (row[1] == '16' and row[5] == '0501') and not (
                row[1] == '53' and row[5] == '1661') and not (row[1] == '53' and row[5] == '1561') and not (
                row[1] == '50' and row[5] == '2791') and all(school != [int(row[1]), int(row[5])] for school in toRemove):

            if row[21] == 'YES':
                # District ID, School ID, District Name, School Name, Lat, Long, Total students
                charters.append([row[1], row[5], row[3], row[6], row[17], row[18], row[37]])
            else:
                others.append([row[1], row[5], row[3], row[6], row[17], row[18], row[37]])
"""
for charter in charters:
    if charter[0]=='21':
        print(":S:DGSD:GH")
        print(charter)
"""
props = []
minprop=1

charterFunds=[]
otherFunds=[]

for i in range(1, 68):
    with open('data/Enrollment/' + str(i) + '.csv') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            # Don't include district totals (0000)
            if row[3] == "Students with Disabilities" and row[2] != '0000':
                for school in charters:
                    if school[1] == row[2] and school[0] == row[1]:
                        if int(row[5])>=10:
                            # SWD count,
                            school.append(row[5])
                            props.append([school[0], school[1], float(school[7]) / float(school[6])])
                            if float(school[7]) / float(school[6])<minprop:
                                minprop=float(school[7]) / float(school[6])
                        charterFunds.append([school[0], school[1],school[3],float(row[5]) / float(school[6])])
                for school in others:
                    if school[1] == row[2] and school[0] == row[1]:
                        school.append(row[5])
                        if int(row[5])>=10:
                            props.append([school[0], school[1], float(school[7]) / float(school[6])])
                        otherFunds.append([school[0], school[1],school[3], float(school[7]) / float(school[6])])

                # print(row)
                # print(row[5])
charterAchievement=copy.deepcopy(charters)
otherAchievement=copy.deepcopy(others)
for i in range(1, 68):
    with open('data/Achievement/' + str(i) + '.csv') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            # Don't include district totals (0000)
            if row[0]=="1819" and row[3] == "Students with Disabilities" and row[2] != '0000':
                for school in charterAchievement:
                    if school[1] == row[2] and school[0] == row[1]:
                        temp=[]
                        for count in range(45,53,2):
                            temp.append(row[count])

                        if "*" not in temp:
                            school.extend(temp)
                for school in otherAchievement:
                    if school[1] == row[2] and school[0] == row[1]:
                        temp = []
                        for count in range(45,53,2):
                            temp.append(row[count])
                        if "*" not in temp:
                            school.extend(temp)


                # print(row)
                # print(row[5])


for i in range(1, 68):
    with open('data/Achievement/' + str(i) + '.csv') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            # Don't include district totals (0000)
            if row[0]=="1819" and row[3] == "Total Students" and row[2] != '0000':
                for school in charterAchievement:
                    if school[1] == row[2] and school[0] == row[1]:
                        temp=[]
                        for count in range(45,53,2):
                            temp.append(row[count])
                        if "*" not in temp:
                            school.extend(temp)
                for school in otherAchievement:
                    if school[1] == row[2] and school[0] == row[1]:
                        temp = []
                        for count in range(45,53,2):
                            temp.append(row[count])
                        if "*" not in temp:
                            school.extend(temp)


#First the SWD data, then the overall popuation of the school data
with open('charterAchievement.csv', 'w') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(["District Name", "School Name", "Lat", "Long","Total Students","Total SWD",'e','s','m','sc','te','ts','tm','tsc'])
    for school in charterAchievement:
        if len(school[2:]) == 14:
            writer.writerow(school[2:])
with open('otherAchievement.csv', 'w') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(["District Name", "School Name", "Lat", "Long","Total Students","Total SWD",'e','s','m','sc','te','ts','tm','tsc'])
    for school in otherAchievement:
        if len(school[2:])==14:
            writer.writerow(school[2:])
# print(charters)
# print(others)
# print(props)[-4:]

with open('data/expenditures.csv') as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
       for charter in charterFunds:
            if charter[0]==row[0] and charter[1]== row[2]:
                charter.append(int(row[10].replace(',', '').replace('$', '')))
       for other in otherFunds:
           if other[0] == row[0] and other[1] == row[2]:
               other.append(int(row[10].replace(',', '').replace('$', '')))

with open('charterFunds.csv', 'w') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(["District", "School","School Name", "prop","funds"])
    for charter in charterFunds:
        writer.writerow(charter)

with open('otherFunds.csv', 'w') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(["District", "School","School Name", "prop","funds"])
    for other in otherFunds:
        writer.writerow(other)


print(minprop)
with open('props.csv', 'w') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(["District", "School", "prop"])
    for prop in props:
        """
        if prop[2] > .999 and prop[2] > 0.69:
            print("and not (row[1] == '" + prop[0] + "' and row[5] == '" + prop[1] + "')", end=' ')
        """
        writer.writerow(prop)
print()
for school in others[:]:
    if len(school) < 8:
        others.remove(school)

for charter in charters[:]:
    if len(charter) < 8:
        #print("a")
        #print(charters[charters.index(charter)])
        #charters.pop(charters.index(charter))
        charters.remove(charter)
clusters = copy.deepcopy(charters)
for cluster in clusters:
    cluster.append([])



#print(clusters)
#print(charters)

for school in others:
    min = 'none'
    for charter in charters:
        if min=='none' and charter[0]==school[0]:
            min=charter
        elif charter[0]==school[0] and (float(school[4]) - float(charter[4])) ** 2 + (float(school[5]) - float(charter[5])) ** 2 < (
                float(school[4]) - float(min[4])) ** 2 + (float(school[5]) - float(min[5])) ** 2:
            min = charter
    # print(min)
    """
    if min=='none':
        print(school)
    if school[0] not in ['02','04',"07",'09','14','15','21']:
        clusters[charters.index(min)][8].append(school)
    """
    if min!='none':
        clusters[charters.index(min)][8].append(school)


print("ACHIEVE")
print(charterAchievement)
for school in otherAchievement[:]:
    if len(school) < 16:
        otherAchievement.remove(school)
for charter in charterAchievement[:]:
    if len(charter) < 16:
        charterAchievement.remove(charter)
print(charterAchievement)
print(otherAchievement)
clusterAchievement=copy.deepcopy(charterAchievement)

for cluster in clusterAchievement:
    cluster.append([])
for school in otherAchievement:
    min = 'none'
    for charter in charterAchievement:
        if min=='none' and charter[0]==school[0]:
            min=charter
        elif charter[0]==school[0] and (float(school[4]) - float(charter[4])) ** 2 + (float(school[5]) - float(charter[5])) ** 2 < (
                float(school[4]) - float(min[4])) ** 2 + (float(school[5]) - float(min[5])) ** 2:
            min = charter
    if min!='none':
        clusterAchievement[charterAchievement.index(min)][16].append(school)



with open('clusterAchievement.csv', 'w') as csvfile:
    writer = csv.writer(csvfile)
    #writer.writerow(["District Name", "School Name", "Lat", "Long","Total Students","Total SWD",'ce1', 'ce2', 'ce3', 'ce4', 'ce5', 'cm1', 'cm2', 'cm3', 'cm4', 'cm5', 'cs1', 'cs2', 'cs3', 'cs4', 'cs5', 'csc1', 'csc2', 'csc3', 'csc4', 'csc5','oe1', 'oe2', 'oe3', 'oe4', 'oe5', 'om1', 'om2', 'om3', 'om4', 'om5', 'os1', 'os2', 'os3', 'os4', 'os5', 'osc1', 'osc2', 'osc3', 'osc4', 'osc5'])
    writer.writerow(["District Name", "School Name", "Lat", "Long","Charter Total Students","Charter Total SWD",'cpe', 'cps', 'cpm', 'cpsc', 'cte', 'cts', 'ctm', 'ctsc',"Other Total Students","Other Total SWD",'ope', 'ops', 'opm', 'opsc', 'ote', 'ots', 'otm', 'otsc'])
    for cluster in clusterAchievement:
        counts = [0,0,0, 0, 0, 0,0,0,0,0]
        for school in cluster[16]:
            # print(school)
            for i in range(10):
                counts[i] += int(school[i + 6])

        cluster = cluster[2:16]
        cluster.extend(counts)
        send = True
        for num in cluster[6:]:
            if int(num) < 10:
                send = True#False
        if send:
            writer.writerow(cluster)
    """
    for cluster in clusterAchievement:
        counts=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
        for school in cluster[48]:
            # print(school)
            for i in range(40):
                counts[i]+=int(school[i+8])
        # District, School, Lat, Long, Charter count, other count, charter total, other tota
        prof=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
        #prof=[cluster[8]+cluster[9]+cluster[10]+cluster[11]+cluster[12],cluster[10]+cluster[11]+cluster[12],cluster[13]+cluster[14]+cluster[15]+cluster[16]+cluster[17],cluster[15]+cluster[16]+cluster[17],cluster[18]+cluster[19]+cluster[20]+cluster[21]+cluster[22],cluster[20]+cluster[21]+cluster[22],cluster[23]+cluster[24]+cluster[25]+cluster[26]+cluster[27],cluster[25]+cluster[26]+cluster[27]]
        for i in range(4):
            for j in range(5):
                prof[2*i]+=int(cluster[8+5*i+j])
            for j in range(2,5):
                prof[2*i+1] += int(cluster[8 + 5 * i + j])

        for i in range(4):
            for j in range(5):
                prof[8+2*i]+=int(counts[5*i+j])
            for j in range(2,5):
                prof[8+2*i+1] += int(counts[5 * i + j])

        cluster=cluster[2:8]
        cluster.extend(prof)
        send=True
        for num in cluster[8:]:
            if int(num)<10:
                send=False
        if send:
            writer.writerow(cluster)
        """


for cluster in clusters:
    for school in cluster[8]:
        if school[0]!=cluster[0]:
            print(cluster)
            print("a")
"""
for school in others:
    min = charters[0]
    for charter in charters:
        if (float(school[4]) - float(charter[4])) ** 2 + (float(school[5]) - float(charter[5])) ** 2 < (
                float(school[4]) - float(min[4])) ** 2 + (float(school[5]) - float(min[5])) ** 2:
            min = charter
    # print(min)
    clusters[charters.index(min)][8].append(school)
"""

"""
for school in others:
    points=charters.copy()
    points.sort(key=lambda K: (float(K[4])-float(school[4])) ** 2 + (float(K[5])-float(school[5])) ** 2)
    print(school)
    print(points[:2])
    for point in points:
        clusters[charters.index(point)][8].append(school)
"""

print(clusters)

# Format is district id, school id, lat, long, total students, swd, [list of the publics in the same format]

alone=0
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
        # District, School, Lat, Long, Charter count, other count, charter total, other total
        if count>=10:
            writer.writerow([cluster[2], cluster[3], cluster[4], cluster[5], cluster[7], count, cluster[6], tot])
        else:
            alone+=1
            print(cluster)
print(alone)
