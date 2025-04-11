import csv
from utils.utils import get_list_names


def Presence(names_detected,count,time):
    names = get_list_names()
    result = [time, count]

    for name in names[2:]:
        if name in names_detected:
            result.append(1)

        else:
            result.append(0)

    with open('Employees.csv', 'a', newline='') as f:

        spamwriter = csv.writer(f, delimiter=',')
        spamwriter.writerow(result)