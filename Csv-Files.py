# Comma seperated values
# It is like a spreadsheet, every line represents a row and each comma a column

import csv
import os

kitteh_csv = os.path.join('Random Files','cat_names.csv')

with open(kitteh_csv, 'w') as f:
    write = csv.writer(f,delimiter=',')
    write.writerow(['Link','Kylo'])
    write.writerow(['Luna','Eris'])

with open (kitteh_csv,'r') as f:
    r = csv.reader(f,delimiter=',')
    for row in r:
        print(','.join(row))