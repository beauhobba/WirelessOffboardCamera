import csv

with open("VBOX202410301159260001.csv", 'r') as f:
    csv_data = csv.reader(f)
    print(csv_data)
    for row in csv_data:
        print(', '.join(row))