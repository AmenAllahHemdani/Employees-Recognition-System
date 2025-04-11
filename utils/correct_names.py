import pandas as pd
import re
from utils.utils import get_list_names


def get_correct_name(list_names,count):
    names = get_list_names()

    df = pd.read_csv('Attendance.csv')
    data = pd.read_csv('Employees.csv')

    null = len(df[df['end_time'] == 'Null'])

    if null == count:
        name = str(df.loc[(df['end_time'] == 'Null') & (df['name'].isin(list_names)==False)].name)
        name = re.findall("[A-Z]\w+", name)[0]

    else:
        occurence = dict()

        for a in [elem for elem in names if elem not in list_names]:
            occurence[a]=len(data[data[a]==1])

        name = max(occurence, key=occurence.get)

    return name
