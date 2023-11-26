import datetime
import json
import csv

import requests


def get_data(my_date: datetime.date) -> str:
    my_year = str(my_date.year)
    my_month = str(my_date.month) if my_date.month > 9 else '0' + \
        str(my_date.month)
    my_day = str(my_date.day) if my_date.day > 9 else '0' + str(my_date.day)
    return my_year + '/' + my_month + '/' + my_day

