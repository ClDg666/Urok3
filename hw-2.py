import json
import time
import pickle
import requests
from bs4 import BeautifulSoup as bs
from pprint import pprint

def save_json(f_name, data):
    with open(f_name, "a", encoding='utf8') as f:
        json.dump(data, f, indent=2, ensure_ascii=False)

def load_json(f_name):
    with open(f_name, "r", encoding='utf8') as f:
        return json.load(f)

def save_pickle(o, path):
    with open(path, 'wb') as f:
        pickle.dump(o, f)


def load_pickle(path):
    with open(path, 'rb') as f:
        return pickle.load(f)


def get(url, headers, param, proxies):
    r = requests.get(url, headers=headers, params=param, proxies=proxies)
    return r


url = 'https://hh.ru/search/vacancy'

appointment = input('Введите должность: ')
# appointment = 'python'


headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.128 Safari/537.36'
}

proxies = {'http': 'http://31.192.159.110'}



i = 0


param = {
    'area': '1', # Сочи
    'text': f'{appointment}',
    "page": f'{i}'
}

r = get(url, headers, param, proxies)
print(r.status_code)

path = 'hh.rsp'
save_pickle(r, path)
r = load_pickle(path)

soup = bs(r.text, "html.parser")


items_all = soup.find_all()

# Определяем число страниц для ввода максимального числа

len_link = soup.find_all(attrs = {"class": "bloko-button", "rel": "nofollow"})
pprint (len_link)
ii = input('Введите количество страниц для сохранения: ')


# print(len(items))

while i < (int(ii)-1):
    param = {
        'area': '1',  # Сочи
        'text': f'{appointment}',
        "page": f'{i}'
    }

    r = get(url, headers, param, proxies)
    soup = bs(r.text, "html.parser")
    items = soup.find_all(attrs={"class": "vacancy-serp-item"})
    j = 0
    while j <= (len(items) - 1):
        string_appoitment = items[j].find("a", attrs={"class": "bloko-link"})
        appointment_href = string_appoitment.attrs["href"]
        appointment_find = string_appoitment.text

        wages_string = items[j].find(attrs={"class": "vacancy-serp-item__sidebar"})
        wages_full = wages_string.text.replace("\u202f", "")
        wages = wages_full.split()

        if len(wages) == 0:
            wages_record = 'з/п не указана'
        elif wages[0] == 'от':
            wages_record = 'min ' + wages[1] + ' ' + wages[-1]
        elif wages[0] == 'до':
            wages_record = 'max ' + wages[1] + ' ' + wages[-1]
        elif wages[0] is None:
            wages_record = 'none'
        else:
            wages_record = 'min ' + wages[0] + ' -  ' + 'max ' + wages[2] + ' ' + wages[-1]

        y = dict(link = appointment_href, appoitment = appointment_find, wages = wages_record)
        y_json = json.dumps(y, ensure_ascii=False)
        print(y_json)
        j += 1
        save_json('file_' + appointment + '.json', y_json)
    i += 1
    save_json('file_' + appointment + '.json', y_json)

