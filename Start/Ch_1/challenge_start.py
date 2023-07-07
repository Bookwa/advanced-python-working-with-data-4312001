# Example file for Advanced Python: Working With Data by Joe Marini
# Programming challenge: summarize the earthquake data

import json


# for this challenge, we're going to summarize the earthquake data as follows:

# 2: How many quakes were felt by at least 100 people?
# 3: Print the name of the place whose quake was felt by the most people, with the # of reports
# 4: Print the top 10 most significant events, with the significance value of each

# open the data file and load the JSON
with open("/workspaces/advanced-python-working-with-data-4312001/30DayQuakes.json", "r") as datafile:
    data = json.load(datafile)

# 1: How many quakes are there in total?
def isAQuake(q):
    if q["properties"]["type"] == "earthquake":
        return True
    return False

events = list(filter(isAQuake, data["features"]))
print(f"Total number of Quake events: {len(events)}")
for i in range(0, 10):
    print(events[i]["properties"]["type"])

print(sum(quake["properties"]["felt"] is not None and quake["properties"]["felt"] >= 100
          for quake in data["features"]))


    