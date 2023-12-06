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


def get_cur_date(my_date: datetime.date) -> str:
    current_date = str(my_date - datetime.timedelta(days=1)).split('-')
    current_datef = current_date[0]+current_date[1]+current_date[2]
    return str(current_datef)


def get_usd() -> None:
    my_date = datetime.date.today()
    current_datef = get_cur_date(my_date)
    my_date -= datetime.timedelta(days=1)
    while my_date.year > 2021:
        begining_data = my_date - datetime.timedelta(days=my_date.weekday())
        begining_data = str(begining_data)[:10]
        begining_dataf = begining_data[:4] + \
            begining_data[5:7]+begining_data[8:10]
        with open(begining_dataf + "_" + current_datef + '.csv', 'a', newline='', encoding="utf-8") as file:
            url = "https://www.cbr-xml-daily.ru/archive/" + \
                get_data(my_date) + "/daily_json.js"
            response = requests.get(url)
            data = json.loads(response.text)
            if 'Valute' not in data:
                if my_date.weekday() == 0:
                    current_datef = get_cur_date(my_date)
                my_date -= datetime.timedelta(days=1)
                continue
            valute_data = data['Valute']
            wr = csv.writer(file)
            for valute in valute_data.values():
                if valute['CharCode'] == 'USD':
                    wr.writerow((f"Дата: {data['Date'][0:10]}").split(','))
                    wr.writerow(
                        (f"{valute['Name']} курс: {valute['Value']}").split(','))
            if my_date.weekday() == 0:
                current_datef = get_cur_date(my_date)
            my_date -= datetime.timedelta(days=1)


def main() -> None:
    get_usd()
