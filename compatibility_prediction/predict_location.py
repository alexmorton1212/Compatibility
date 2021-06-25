import csv

caregiver_city = input("Caregiver City: ")
caregiver_state = input("Caregiver State: ")
careseeker_city = input("Careseeker City: ")
careseeker_state = input("Careseeker State: ")

caregiver_county = ""
careseeker_county = ""

with open("city_county.csv") as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    for row in csv_reader:
        if row[0].lower() == caregiver_city.lower() and row[1].lower() == caregiver_state.lower():
            caregiver_county = row[3] + " County"
        if row[0].lower() == careseeker_city.lower() and row[1].lower() == careseeker_state.lower():
            careseeker_county = row[3] + " County"

caregiver_county_gop = 0
caregiver_county_dem = 0
careseeker_county_gop = 0
careseeker_county_dem = 0
caregiver_total = 0
careseeker_total = 0
caregiver_loc_perc = 0
careseeker_loc_perc = 0

with open("2016_US_County_Level_Presidential_Results.csv") as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    for row in csv_reader:
        if row[9].lower() == caregiver_county.lower() and row[8].lower() == caregiver_state.lower():
            caregiver_county_gop = row[5]
            caregiver_county_dem = row[4]
        if row[9].lower() == careseeker_county.lower() and row[8].lower() == careseeker_state.lower():
            careseeker_county_gop = row[5]
            careseeker_county_dem = row[4]

location_difference = 1 - abs(float(caregiver_county_dem) - float(careseeker_county_dem))

