import csv
import pandas as pd
import datetime



def get_list_names():
    names = ['time','count','Alice','Lydia','Alison','Scott']
    return names

def inisialize_csv_file():
    names = get_list_names()

    with open('Employees.csv', 'w', newline = '') as f:
        spamwriter = csv.writer(f, delimiter = ',')
        spamwriter.writerow(names)

def fill_null_date():

    time = datetime.datetime.now().strftime('%H:%M:%S')

    df = pd.read_csv('Attendance.csv')

    index = df.index[df['end_time'] == 'Null'].tolist()

    for i in index:
        df.loc[i , 'end_time'] = time

    df.to_csv('Attendance.csv')
