import requests
import csv


def get_weather_data(station_code, date_str, output_file):
    year, month, day = date_str.split('-')
    url = f'https://mesonet.agron.iastate.edu/cgi-bin/request/asos.py?station={station_code}&data=all&year1={year}&month1={month}&day1={day}&year2={year}&month2={month}&day2={day}&tz=Etc%2FUTC&format=onlycomma&latlon=no&direct=no&report_type=1&report_type=2'
    response = requests.get(url)
    data = response.content.decode('utf-8')

    rows = csv.reader(data.splitlines())
    with open(output_file, 'w', newline='') as csv_file:
        writer = csv.writer(csv_file)
        for row in rows:
            writer.writerow(row)


get_weather_data('LFMD', '2023-04-19', 'weather_data.csv')
