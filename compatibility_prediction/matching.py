import csv
import json
import operator
import urllib.request


### Gets text from user inputs
caregiver_input = input("Caregiver Text: ")
caregiver_input = caregiver_input.replace(" ", "+")
careseeker_input = input("Careseeker Text: ")
careseeker_input = careseeker_input.replace(" ", "+")


# myersbriggs()
### takes in two chunks of texts (that the user manually types at the moment)
### uses uClassify API to determine the MBTI type of both inputs
### calculates compatibility based on MyersBriggs_Compatibility.csv
### returns value 0-1 (1 being "perfect" compatibility)

def myersbriggsAPI():
    myers_url = "https://api.uclassify.com/v1/g4mes543/myers-briggs-type-indicator-text-analyzer/classify/?readKey=kdCYczikJWST&text="

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

    ### returns Compatibility of Two types ###
    with open("MyersBriggs_Compatibility.csv") as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        for row in csv_reader:
            if row[0] == types:
                return float(row[5])
            if row[0] == reverse_types and types != reverse_types:
                return float(row[5])


# politicize()
### takes in two chunks of texts (that the user manually types at the moment)
### uses uClassify API to determine the predicted liberal and conservative percentage of both inputs
### calculates compatibility based on distance between each percentage
### returns value 0-1 (1 being exact same scores, 0 being exact opposite)

def politicalAPI():
    politics_url = "https://api.uclassify.com/v1/Politimind/Liberal-or-conservative/classify/?readKey=kdCYczikJWST&text="

    ### Create correct URL's to apply uClassify API
    caregiver_url = politics_url + caregiver_input
    careseeker_url = politics_url + careseeker_input

    ### Runs Political Ideology test on writing samples
    with urllib.request.urlopen(caregiver_url) as url:
        caregiver_data = json.loads(url.read().decode())
    with urllib.request.urlopen(careseeker_url) as url:
        careseeker_data = json.loads(url.read().decode())

    ### Calculates liberal and conservative percentages based on texts
    caregiver_con = caregiver_data.get('Conservative')
    caregiver_lib = caregiver_data.get('Liberal')
    careseeker_con = careseeker_data.get('Conservative')
    careseeker_lib = careseeker_data.get('Liberal')

    ### Final value based on distance between one of the ideologies
    ### Could use either but since sum of the two (con and lib) adds up to 1 it doesn't matter
    return 1 - abs(caregiver_lib - careseeker_lib)


# locations()
### asks for the city & state that the user is from (user manually types at the moment)
### this city & state could also be their favorite place that they've lived
### uses 2016_US_County(...).csv and city_county.csv to determine political culture of that place
### calculates compatibility based on distance between each percentage
### returns value 0-1 (1 being exact same scores)

def locations():
    ### Loads inputs (eventually) from Caregiver and Careseeker applications
    cg_city = input("Caregiver City: ")
    cg_state = input("Caregiver State: ")
    cs_city = input("Careseeker City: ")
    cs_state = input("Careseeker State: ")

    cg_county = ""
    cs_county = ""

    ### Determines county based on city and state inputs
    with open("city_county.csv") as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        for row in csv_reader:
            if row[0].lower() == cg_city.lower() and (
                    row[1].lower() == cg_state.lower() or row[2].lower() == cg_state.lower()):
                cg_state = row[1].lower()
                cg_county = row[3] + " County"
            if row[0].lower() == cs_city.lower() and (
                    row[1].lower() == cs_state.lower() or row[2].lower() == cs_state.lower()):
                cs_state = row[1].lower()
                cs_county = row[3] + " County"

    cg_county_gop = 0
    cg_county_dem = 0
    cs_county_gop = 0
    cs_county_dem = 0

    ### Determines election results from the county based on county and state
    with open("2016_US_County_Level_Presidential_Results.csv") as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        for row in csv_reader:
            if row[9].lower() == cg_county.lower() and row[8].lower() == cg_state.lower():
                cg_county_gop = row[5]
                cg_county_dem = row[4]
            if row[9].lower() == cs_county.lower() and row[8].lower() == cs_state.lower():
                cs_county_gop = row[5]
                cs_county_dem = row[4]

    ### Final value based on distance between one of the ideologies
    ### Could use either but since sum of the two (dem and gop) adds up to 1 it doesn't matter
    return 1 - abs(float(cg_county_dem) - float(cs_county_dem))


# interests()
### this one is not very worked out
### potential idea is to have 10 options for interests and get the user to select the top 3
### asks for 3 interests from the user (right now type in, eventually select from list)
### compares these 3 interests to the top 3 interests of the potentially caregivers
### returns highest compatibility value (0-1) based on how many are alike
### only returns the highest value right now

def interests():
    ### data.json is a file I created to play around with
    f = open('data.json', )
    data = json.load(f)

    ### asks the user for 3 interests (ex. music, running, etc.)
    input1 = input("Interest 1: ")
    input2 = input("Interest 2: ")
    input3 = input("Interest 3: ")

    length = len(data)
    interest_count_array = [0] * length

    ### compares user (careseeker) data to a database of caregivers
    count = 0
    for x in data:
        if data[count]['interest1'] == input1 or data[count]['interest1'] == input2 or data[count][
            'interest1'] == input3:
            interest_count_array[count] += 1
        if data[count]['interest2'] == input1 or data[count]['interest2'] == input2 or data[count][
            'interest2'] == input3:
            interest_count_array[count] += 1
        if data[count]['interest3'] == input1 or data[count]['interest3'] == input2 or data[count][
            'interest3'] == input3:
            interest_count_array[count] += 1
        count += 1

    newArray = interest_count_array

    ### assigns a compatibility score between each caregiver and careseeker
    count = 0
    for x in interest_count_array:
        if interest_count_array[count] == 3:
            newArray[count] = 0.99
        if interest_count_array[count] == 2:
            newArray[count] = 0.89
        if interest_count_array[count] == 1:
            newArray[count] = 0.79
        count += 1

    return max(newArray) + 0.01


# calculate_compatibility
### returns final compatibility value based on formula
def calculate_compatibility():
    return (0.25*myersbriggsAPI()) + (0.15*politicalAPI()) + (0.30*interests()) + (0.30*locations())


print(calculate_compatibility())
