import requests
from bs4 import BeautifulSoup
import pandas as pd
import scrap_lattes
import os
BASE_URL = 'https://ebape.fgv.br'
urls = ['/corpo-docente', '/en/faculty', '/es/cuerpo-docente']
col = ["url","position","prof", "prof_link", "prof_link_short","name","updated_at","programs","image","contact","links","body"]


def get_prof_list():
    profs_list = []
    for url in urls:
        content = requests.get(BASE_URL + url).content
        soup = BeautifulSoup(content, 'html.parser')
        box = soup.find("div",{"class":"view-content"})
        containers = box.find_all("div","item-list")
        for container in containers:
            position = container.find("h3").text
            profs = container.find_all("span","field-content")
            for prof in profs:
                profs_list.append((url,position,prof.text.strip(), prof.find("a").get("href"), prof.find("a").get("href").split("/")[-1]))
    return profs_list

def get_lattes(text):
    cv_list = os.listdir("CVs\\")
    if 'lattes.cnpq.br' in text:
        file = text.split('/')[-1]+'.html'
        if file not in cv_list:
            scrap_lattes.solve_captcha(text)
    return text

def get_details(prof):
    try:
        content = requests.get(BASE_URL + prof[3]).content
        soup = BeautifulSoup(content, 'html.parser')
        name = soup.find("section", {"id": "main-content"}).find("h1").text.strip()
        updated_at = soup.find("div", {"class": "updated-at"}).text.strip()
        node_content = soup.find("div", {"class": "node-content"})
        try:
            links = '\n'.join([get_lattes(link.find("a").get("href")) for link in node_content.find_all("div", {"class": "field-type-link-field"})])
        except:
            links = ''
        image = node_content.find("img").get("src")
        try:
            contact = '\n'.join([info.text.strip() for info in node_content.find("section", {"class": "field-name-field-docente-informacoes"}).find("div", {"class": "field-item"}).find_all("a")])
        except:
            contact = ''
        try:
            programs ='\n'.join( [info.text.strip() for info in node_content.find("section", {"class": "field-name-field-docente-programa"}).find_all("div", {"class": "field-item"})])
        except:
            programs = ''
        try:
            body = '\n'.join([info.text.strip() for info in node_content.find("div", {"class": "field-name-body"}).find_all("div", {"class": "field-item"})])
        except:
            body = ''
        return tuple(list(list(prof) + list([name,updated_at,programs,image,contact,links,body])))
    except Exception as e:
        print(prof[3],e)


prof_list = [get_details(x) for x in get_prof_list()]
table = pd.DataFrame(prof_list, columns=col)
table.to_excel('ebape_prof.xls','EBAPE')
