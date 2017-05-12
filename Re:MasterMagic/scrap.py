# -*- coding: utf-8 -*-
__author__ = 'Carlobo'

from bs4 import BeautifulSoup
import requests, os, re

link_chapters = []
link_volumes = []
volume_names = []
URL = "https://lightnovelstranslations.com/re-master-magic/"

if not os.path.exists("Chapters"):
    os.makedirs("Chapters")
if not os.path.exists("Volumes"):
    os.makedirs("Volumes")
# Realizamos la petición a la web
req = requests.get(URL)

# Comprobamos que la petición nos devuelve un Status Code = 200
status_code = req.status_code
if status_code == 200:

    # Pasamos el contenido HTML de la web a un objeto BeautifulSoup()
    html = BeautifulSoup(req.text, "html5lib")

    # Obtenemos todos los divs donde están las entradas
    volumes = html.find_all('div', {'class': re.compile("su-spoiler su-spoiler-style-default su-spoiler-icon-plus*")})
    for i,volume in enumerate(volumes):
        volume_name = volume.find('div', {'class': 'su-spoiler-title'}).getText()
        chapters = volume.find('div', {'class': 'su-spoiler-content su-clearfix'})
        links = chapters.find_all('a')
        for j,link in enumerate(links):
            link_chapters.append(link.get('href'))
        link_volumes.append(link_chapters)
        volume_names.append(volume_name)
        link_chapters = []

else:
    print "Status Code %d" % status_code

for i,links in enumerate(link_volumes):
    fileVolu = open("Volumes/"+volume_names[i], 'w');
    for j,link in enumerate(links):
        URL = link
        req = requests.get(URL)
        status_code = req.status_code
        if status_code == 200:
            html = BeautifulSoup(req.text, "html5lib")
            title = html.find('h1', {'class': 'entry-title'}).getText()
            file = open("Chapters/"+title, 'w');
            chapter = html.find('div', {'class': 'entry-content'})
            file.write(chapter.getText().encode("utf-8")+"\n")
            fileVolu.write(chapter.getText().encode("utf-8")+"\n")
            file.close()
        else:
            print "Status Code %d" % status_code
    fileVolu.close()
