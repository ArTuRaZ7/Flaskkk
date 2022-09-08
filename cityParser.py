import requests
from bs4 import BeautifulSoup
import csv

def millionaires():
    html = BeautifulSoup(requests.get("https://города-россия.рф/reytin-cities.php?name=миллионеры").text, "html.parser")
    div = html.find("div", id='text-l').find_all('li')
    with open('csv/millionairesCities.csv', "w", newline='', encoding='utf-8') as f:
        writer = csv.writer(f, delimiter=',')
        for i in range(len(div)):
            li = BeautifulSoup(str(div[i]), 'html.parser')
            city = li.find('a').get_text()
            value = li.find('span').get_text()
            value = ''.join([i for i in value if i.isdigit()])
            writer.writerow([city, value])


def biggest():
    html = BeautifulSoup(requests.get("https://города-россия.рф/reytin-cities.php?name=крупнейшие").text, "html.parser")
    div = html.find("div", id='text-l').find_all('li')
    with open('csv/biggestCities.csv', "w", newline='', encoding='utf-8') as f:
        writer = csv.writer(f, delimiter=',')
        for i in range(len(div)):
            li = BeautifulSoup(str(div[i]), 'html.parser')
            city = li.find('a').get_text()
            value = li.find('span').get_text()
            value = ''.join([i for i in value if i.isdigit()])
            writer.writerow([city, value])


def big():
    html = BeautifulSoup(requests.get("https://города-россия.рф/reytin-cities.php?name=крупные").text, "html.parser")
    div = html.find("div", id='text-l').find_all('li')
    with open('csv/bigCities.csv', "w", newline='', encoding='utf-8') as f:
        writer = csv.writer(f, delimiter=',')
        for i in range(len(div)):
            li = BeautifulSoup(str(div[i]), 'html.parser')
            city = li.find('a').get_text()
            value = li.find('span').get_text()
            value = ''.join([i for i in value if i.isdigit()])
            writer.writerow([city, value])


def large():
    html = BeautifulSoup(requests.get("https://города-россия.рф/reytin-cities.php?name=большие").text, "html.parser")
    div = html.find("div", id='text-l').find_all('li')
    with open('csv/largeCities.csv', "w", newline='', encoding='utf-8') as f:
        writer = csv.writer(f, delimiter=',')
        for i in range(len(div)):
            li = BeautifulSoup(str(div[i]), 'html.parser')
            city = li.find('a').get_text()
            value = li.find('span').get_text()
            value = ''.join([i for i in value if i.isdigit()])
            writer.writerow([city, value])


def medium():
    html = BeautifulSoup(requests.get("https://города-россия.рф/reytin-cities.php?name=средние").text, "html.parser")
    ol = html.find("ol", attrs={"style":"background-color: rgb(255, 255, 255);"}).find_all('li')
    with open('csv/mediumCities.csv', "w", newline='', encoding='utf-8') as f:
        writer = csv.writer(f, delimiter=',')
        for i in range(len(ol)):
            li = BeautifulSoup(str(ol[i]), 'html.parser')
            try:
                city = li.find('a').get_text()
            except:
                city = li.find('strong').get_text().split()[0]
            value = li.find('span').get_text()
            value = ''.join([i for i in value if i.isdigit()])
            writer.writerow([city, value])


def small():
    html = BeautifulSoup(requests.get("https://города-россия.рф/reytin-cities.php?name=малые").text, "html.parser")
    ol = html.find("ol", attrs={"style":"background-color: rgb(255, 255, 255);"}).find_all('li')
    with open('csv/smallCities.csv', "w", newline='', encoding='utf-8') as f:
        writer = csv.writer(f, delimiter=',')
        for i in range(len(ol)):
            li = BeautifulSoup(str(ol[i]), 'html.parser')
            try:
                city = li.find('a').get_text()
            except:
                try:
                    city = li.find('strong').get_text().split()[0]
                except:
                    city = li.find('b').get_text().split()[0]
            value = li.find('span').get_text()
            value = ''.join([i for i in value if i.isdigit()])
            writer.writerow([city, value])


millionaires()
biggest()
big()
large()
medium()
small()
