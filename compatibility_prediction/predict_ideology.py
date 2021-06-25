import csv
import json
import operator
import urllib.request

politics_url = "https://api.uclassify.com/v1/Politimind/Liberal-or-conservative/classify/?readKey=kdCYczikJWST&text="

### Load inputs from Caregiver and Careseeker application responses ###

caregiver_input = input("Caregiver Text: ")
caregiver_input = caregiver_input.replace(" ", "+")
careseeker_input = input("Careseeker Text: ")
careseeker_input = careseeker_input.replace(" ", "+")

### Create correct URL's to apply uClassify API ###

caregiver_url = politics_url + caregiver_input
careseeker_url = politics_url + careseeker_input

### Runs Political Ideology test on writing samples ###

with urllib.request.urlopen(caregiver_url) as url:
    caregiver_data = json.loads(url.read().decode())
with urllib.request.urlopen(careseeker_url) as url:
    careseeker_data = json.loads(url.read().decode())

caregiver_con = caregiver_data.get('Conservative')
caregiver_lib = caregiver_data.get('Liberal')
careseeker_con = careseeker_data.get('Conservative')
careseeker_lib = careseeker_data.get('Liberal')

caregiver_net = caregiver_lib - caregiver_con
careseeker_net = careseeker_lib - careseeker_con

politic_compatibility = abs((caregiver_net + careseeker_net)/2)

print(politic_compatibility)



