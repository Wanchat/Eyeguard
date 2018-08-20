import csv
import random

def writ_csv(csv_name,list):
    with open(csv_name,'w', newline='') as f:
        reader = csv.writer(f, delimiter= ',')
        data = list
        reader.writerows(data)

if __name__ == '__main__':
    i = [i for i in range(100)]
    writ_csv('test_csv.csv', i)




