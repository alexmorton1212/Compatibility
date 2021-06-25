import json

f = open('data.json',)
data = json.load(f)

input1 = input("Interest 1: ")
input2 = input("Interest 2: ")
input3 = input("Interest 3: ")

length = len(data)
interest_count_array = [0] * length

count = 0
for x in data:
    if data[count]['interest1'] == input1 or data[count]['interest1'] == input2 or data[count]['interest1'] == input3:
        interest_count_array[count] += 1
    if data[count]['interest2'] == input1 or data[count]['interest2'] == input2 or data[count]['interest2'] == input3:
        interest_count_array[count] += 1
    if data[count]['interest3'] == input1 or data[count]['interest3'] == input2 or data[count]['interest3'] == input3:
        interest_count_array[count] += 1
    count += 1

newArray = [0] * length

count = 0
for x in interest_count_array:
    if interest_count_array[count] == 3:
        newArray[count] = 0.99
    if interest_count_array[count] == 2:
        newArray[count] = 0.89
    if interest_count_array[count] == 1:
        newArray[count] = 0.79
    count += 1

print(newArray)

f.close()
