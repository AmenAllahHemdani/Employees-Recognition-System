import pandas as pd
import datetime
from utils.utils import get_list_names


def compare_time(end_time,time):
    s1 = datetime.datetime.strptime(end_time,'%H:%M:%S')
    s2 = datetime.datetime.strptime(time,'%H:%M:%S')

    duration = abs(s1-s2)

    return duration.total_seconds()<20


def Attendance(count,date,time):
    names = get_list_names()

    df = pd.read_csv('Attendance.csv')
    data = pd.read_csv('Employees.csv')

    df = df[['date','name','start_time','end_time']]

    data = data[data['time'] == time]
    null = len(df[df['end_time'] == 'Null'])

    for name in names[2:]:
        i=len(df)
        if df.isin([name]).any().any():
            index = df.index[df['name'] == name].tolist()[-1]
            end_time = df.loc[index].end_time

            if (end_time == 'Null') and (len(data[data[name].isin([1])]) == 0) and (null > count):
                df.loc[index, 'end_time'] = time

            elif (end_time != 'Null') and (len(data[data[name].isin([1])]) > 2):
                if compare_time(end_time, time):
                    df.loc[index , 'end_time'] = 'Null'

                else:
                    result = [date, name, time, 'Null']

                    if len(data[data[name].isin([1])]) > 0:
                        df.loc[i] = result

        elif (len(data[data[name].isin([1])]) > 2) and not (df.isin([name]).any().any()):
            result = [date, name, time, 'Null']

            if len(data[data[name].isin([1])])>0:
                df.loc[i] = result

    df.to_csv('Attendance.csv')

