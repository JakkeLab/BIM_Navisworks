#import modules
from turtle import title
from bs4 import BeautifulSoup
import csv

#Importing report file (HTML)
html = open(r"C:\Users\sjak3\Desktop\JAKK3LAB\DEV\BIM\4D\1_ClashDetectiveSelector\0-2_ReportFile\1_레이커-보+기둥.html", 'r', encoding='UTF8')

#Set the CSV File form. File should not have any blank rows(newline='').
csvFile = open('Report.csv', "w", newline='',encoding="utf-8-sig")

#Set object as 'soup'
soup = BeautifulSoup(html, "html.parser")

#Every clash is divided by 'div' tag, whose class value is 'viewpoint'
div_clash = soup.find_all('div', class_='viewpoint')

#For counting the number of loop
list_count =len(div_clash)
clashSets = []

for i in range(0, list_count):
    #Between 'div' tags, 'span' tags contain the information of each elements.
    clashTags = div_clash[i].find_all('span', class_='value')
    
    #In my case, clash number is on the index '0', first object's ID on '6', second object on '13'
    clashSets.append([clashTags[0].get_text(), clashTags[6].get_text(), clashTags[13].get_text()])

#Write on CSV File
csvFileW = csv.writer(csvFile)

#Set the field at the first row.
csvFileW.writerow(["간섭번호", "개체1", "개체2"])

#Add all clash informations.
for i in range(0, len(clashSets)):
    csvFileW.writerow(clashSets[i])

csvFile.close()
