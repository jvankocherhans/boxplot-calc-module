import csv

dataValues = []

with open('./data/data.csv', 'r') as file:
    csvReader = csv.reader(file)
    
    string_to_int = lambda x: int(x)

    for row in csvReader:
        int_row = list(map(string_to_int, row))
        dataValues.append(int_row)
