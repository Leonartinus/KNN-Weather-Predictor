import csv

p = r"C:\Users\leogl\OneDrive - UBC\Desktop\CS project\ML\RW\2021.csv" ## path of the file

def reader(path):
## (String -> List)
## Read the file and put the data into a list

    rows = [] 

    with open(path) as f: 
        f_csv =csv.reader(f)
        
        for row in f_csv:
            rows.append(row)
        
    rows.pop(0) 

    return rows 

def parse_floats(rows: list): 
## (list -> list)
## convert the strings in the list into Float

    for row in rows:
        for i in range(7):
            if row[i] == "":
                row[i] = 0.0
            else:
                row[i] = float(row[i])

    return rows

def parse_rain(rows: list):
## (list -> list)
## convert the strings that contains "Rain" into True, else False

    for row in rows:
        if "Rain" in row[7]:
            row[7] = True
        else:
            row[7] = False

    return rows

def parse(rows: list):
## (list -> list)
## convert the list of strings into the list with float number and boolean

    rows = parse_rain(parse_floats(rows))

    return rows

rows = parse(reader(p))

def new_data_structue(data_set):
## (list -> list)
## produce the list rows that contains the information that 2 rows before

    new_data = []

    for i in range(2, len(data_set)):
        new_data.append(data_set[i-2] + data_set[i-1] + [data_set[i][7]])
    
    return new_data

new_data = new_data_structue(rows)

header = ["Temp (°C) -2h", "Dew Point Temp (°C) -2h", "Rel Hum (%) -2h"
        , "Wind Dir (10s deg) -2h", "Wind Spd (km/h) -2h"
        , "Visibility (km) -2h", "Stn Press (kPa) -2h", "Weather -2h",

          "Temp (°C) -1h", "Dew Point Temp (°C) -1h", "Rel Hum (%) -1h"
        , "Wind Dir (10s deg) -1h", "Wind Spd (km/h) -1h"
        , "Visibility (km) -1h", "Stn Press (kPa) -1h", "Weather -1h",

                                                      "Weather"]

def writer():
## write the new data into a new csv file

    with open("2021 historical climate data.csv", "w", encoding="UTF8", newline="") as f_:
        writer = csv.writer(f_)

        writer.writerow(header)

        writer.writerows(new_data)