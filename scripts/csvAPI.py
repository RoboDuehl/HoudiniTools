import csv

points = [
        [0, 1.1, 1.2, 1.3],
        [1, 0.5, 1.0, 1.0],
]

filename = 'points.csv'

with open(filename, 'w', newline="") as file:
    writer = csv.writer(file)
    
    writer.writerow(["ID", "X", "Y", "Z"])

    for point in point:
        writer.writerow(point)

print(f"Points have been written to {filename}")
