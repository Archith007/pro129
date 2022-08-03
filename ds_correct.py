import csv
data = []

with open ("dwarf_updated.csv","r") as f:
    csvreader = csv.reader(f)
    
    for i in csvreader:
        data.append(i)

headers = data[0]
sun_data = data[1:]

for i in sun_data:
    i[3] = float(i[3])*0.000954588
    i[4] = float(i[4])*0.000954588

with open ("dwarf_corrected.csv", "a+") as f:
    csvwriter = csv.writer(f)

    csvwriter.writerow(headers)
    csvwriter.writerows(sun_data)

with open('dwarf_corrected.csv') as input, open('dwarf_corrected1.csv', 'w', newline='') as output:
    writer = csv.writer(output) 
    for row in csv.reader(input): 
        if any(field.strip() for field in row): 
            writer.writerow(row)