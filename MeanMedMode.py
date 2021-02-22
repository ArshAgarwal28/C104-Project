from collections import Counter
import csv

with open(r"C:\Users\arsh.agarwal\OneDrive\WhiteHat\Python\WhiteHat Projects\C104\HeightWeightData.csv") as f:
    reader = csv.reader(f)
    file_data = list(reader)

file_data.pop(0)

weight_total = 0
weight_array = []

for index in range(len(file_data)):
    weight_array.append(file_data[index][2])
    weight_total += float(file_data[index][2])

weight_array.sort()

mean = weight_total / len(weight_array)

median = 0

if len(weight_array) % 2:
    mid_index = len(weight_array) / 2
    num1 = weight_array[mid_index]
    num2 = weight_array[mid_index - 1]

    median = (num1 + num2) / 2

else:
    mid_index = len(weight_array) // 2
    median = weight_array[mid_index]

item_count = Counter(weight_array)

data_range = {
    "90 - 100": 0,
    "100 - 110": 0,
    "110 - 120": 0,
    "120 - 130": 0,
    "130 - 140": 0,
    "140 - 150": 0,
    "150 - 160": 0,
    "160 - 170": 0,
}


for weight, occurrence in item_count.items():
    if 90 < float(weight) < 100:
        data_range["90 - 100"] += occurrence

    elif 100 < float(weight) < 110:
        data_range["100 - 110"] += occurrence

    elif 110 < float(weight) < 120:
        data_range["110 - 120"] += occurrence

    elif 120 < float(weight) < 130:
        data_range["120 - 130"] += occurrence

    elif 130 < float(weight) < 140:
        data_range["130 - 140"] += occurrence

    elif 140 < float(weight) < 150:
        data_range["140 - 150"] += occurrence

    elif 150 < float(weight) < 160:
        data_range["150 - 160"] += occurrence

    elif 160 < float(weight) < 170:
        data_range["160 - 170"] += occurrence

