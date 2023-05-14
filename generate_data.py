import csv
import random


attributes = ['Sales', 'CompPrice', 'Income', 'Advertising', 'Population', 'Price', 'ShelveLoc', 'Age', 'Education', 'Urban', 'US']
data = []
for _ in range(400):
    row = [
        round(random.uniform(5, 25), 1),
        random.randint(100, 200),
        random.randint(10, 100),
        random.randint(1, 20),
        random.randint(100, 500),
        random.randint(50, 200),
        random.choice(['Bad', 'Good', 'Medium']),
        random.randint(20, 60),
        random.randint(8, 16),
        random.choice(['Yes', 'No']),
        random.choice(['Yes', 'No'])
    ]
    data.append(row)

filename = 'generated_data.csv'
with open(filename, 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(attributes)
    writer.writerows(data)
