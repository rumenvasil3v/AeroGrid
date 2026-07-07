import csv

flag_anomalies_turbine_ids = []
dictionary_turbines = {}
dictionary_turbines_temp_count = {}

dictionary_turbines_vibration = {}
dictionary_turbines_vibration_count = {}

with open("telemetry.csv") as csvfile:
    data = csv.reader(csvfile)

    first_line = 0

    for row in data:
        print(row)

        if first_line == 0:
            first_line = 1
            continue

        turbine_id = row[1]
        temperature_current_turbine = float(row[2])
        vibration_current_turbine = float(row[3])

        if turbine_id not in dictionary_turbines:
            dictionary_turbines[turbine_id] = temperature_current_turbine
            dictionary_turbines_vibration[turbine_id] = vibration_current_turbine
            dictionary_turbines_temp_count[turbine_id] = 1
            dictionary_turbines_vibration_count[turbine_id] = 1
        else:
            dictionary_turbines[turbine_id] += temperature_current_turbine
            dictionary_turbines_vibration[turbine_id] += vibration_current_turbine
            dictionary_turbines_temp_count[turbine_id] += 1
            dictionary_turbines_vibration_count[turbine_id] += 1

for key, value in dictionary_turbines.items():
    current_temp = value / dictionary_turbines_temp_count[key]

    if current_temp > 85.0:
        print("Average temp for " + key + " is " + str(current_temp))
        flag_anomalies_turbine_ids.append(key)

for key, value in dictionary_turbines_vibration.items():
    current_vibration = value / dictionary_turbines_vibration_count[key]

    if current_vibration > 15.0:
        print("Average vibration for " + key + " is " + str(current_vibration))
        flag_anomalies_turbine_ids.append(key)

unique_turbine_ids = list(set(flag_anomalies_turbine_ids))

for id in unique_turbine_ids:
    print("Turbine ID needed for urgent maintenance: " + id)

# anomaly is data point that deviates from what is normal or safe
# urgent maintenance if exceeds 85.0 degrees in Celsius
# vibration levels spike above 15.0 mm/s
# usually library 'pandas' is the industry standard for handling massive spreadsheets and CSV files efficiently