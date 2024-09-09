import csv

def generate_new_row(row, noise_level=0.01):
    # Add noise to each feature to generate a new row
    new_row = [float(value) * (1 + noise_level) for value in row[:-1]]
    new_row.append(row[-1])
    return new_row

with open('output.csv', 'r') as infile:
    reader = csv.reader(infile)
    original_data = [row for row in reader]

additional_rows = 9000000
new_data = original_data.copy()

# Generate new rows by slightly modifying existing rows
for i in range(additional_rows):
    new_row = generate_new_row(original_data[i % len(original_data)])
    new_data.append(new_row)

with open('dataset.csv', 'w', newline='') as outfile:
    writer = csv.writer(outfile)
    writer.writerows(new_data)
