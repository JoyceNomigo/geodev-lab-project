# import csv

# with open('my_data.csv', encoding='utf-8-sig') as f:
#     reader = csv.DictReader(f)
#     rows = list(reader)

# values = []
# for row in rows:
#     raw = row["area_km2"].strip()
#     if raw == "":
#         continue
#     values.append(float(raw))

# print("largest value: ", max(values))
# print("smallest value", min(values))
# print("count: ", len(values))

from csv import DictReader
import csv


def inspect_column(filename, column):
    with open(filename, encoding="utf-8-sig") as f:
              rows = list(csv.DictReader(f))
    values = []
    for row in rows:
        raw = row[column].strip()
        if raw == "":
            continue
        values.append(float(raw))
    return{
        "smallest": min(values),
        "largest": max(values),
        "count": len(values),
    }

area_result = inspect_column("my_data.csv", "area_km2")
pop_result = inspect_column("my_data.csv", "population")

print ("area_km2:", area_result)
print ("Population:", pop_result)

        