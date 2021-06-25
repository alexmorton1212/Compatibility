import csv
import json
import operator
import urllib.request

myers_url = "https://api.uclassify.com/v1/g4mes543/myers-briggs-type-indicator-text-analyzer/classify/?readKey=kdCYczikJWST&text="

### Load inputs from Caregiver and Careseeker application responses ###

caregiver_input = input("Caregiver Text: ")
caregiver_input = caregiver_input.replace(" ", "+")
careseeker_input = input("Careseeker Text: ")
careseeker_input = careseeker_input.replace(" ", "+")

### Create correct URL's to apply uClassify API ###

caregiver_url = myers_url + caregiver_input
careseeker_url = myers_url + careseeker_input

### Runs Myers-Brigg test on writing samples ###

with urllib.request.urlopen(caregiver_url) as url:
    caregiver_data = json.loads(url.read().decode())
with urllib.request.urlopen(careseeker_url) as url:
    careseeker_data = json.loads(url.read().decode())

### returns Highest Rated Myers-Briggs Types ###

myers_type_caregiver = max(caregiver_data.items(), key=operator.itemgetter(1))[0]
myers_type_careseeker = max(careseeker_data.items(), key=operator.itemgetter(1))[0]
types = myers_type_caregiver + "-" + myers_type_careseeker
reverse_types = myers_type_careseeker + "-" + myers_type_caregiver
print("Caregiver Type: " + myers_type_caregiver)
print("Careseeker Type: " + myers_type_careseeker)

### returns Compatibility of Two types ###

myers_compatibility = 0

with open("MyersBriggs_Compatibility.csv") as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    for row in csv_reader:
        if row[0] == types:
            print(row[5])
            myers_compatibility = row[5]
        if row[0] == reverse_types and types != reverse_types:
            print(row[5])
            myers_compatibility = row[5]

