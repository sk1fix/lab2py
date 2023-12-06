import datetime
import json

import requests


def get_data(my_date: datetime.date) -> str:
    my_year = str(my_date.year)
    my_month = str(my_date.month) if my_date.month > 9 else '0' + \
        str(my_date.month)
    my_day = str(my_date.day) if my_date.day > 9 else '0' + str(my_date.day)
    return my_year + '/' + my_month + '/' + my_day

def get_usd(my_date:datetime.date) -> str:
    url = "https://www.cbr-xml-daily.ru/archive/" + \
                get_data(my_date) + "/daily_json.js"
    response = requests.get(url)
    data = json.loads(response.text)
    if 'Valute' not in data:
        return None
    valute_data = data['Valute']
    for valute in valute_data.values():
        if valute['CharCode'] == 'USD':
            rate=(f"{valute['Name']} курс: {valute['Value']}")
    return rate
