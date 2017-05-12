# -*- coding: utf-8 -*-
__author__ = 'Carlobo'

from bs4 import BeautifulSoup
import requests
import os


URL_prueba ="https://web.archive.org/web/20141015154755/http://www.royalroadl.com:80/legendary-moonlight-sculptor-volume-2/"

URLs_royalroadl = ['https://web.archive.org/web/20141015153325/http://www.royalroadl.com:80/legendary-moonlight-sculptor-volume-1/',
        'https://web.archive.org/web/20141015154755/http://www.royalroadl.com:80/legendary-moonlight-sculptor-volume-2/',
        'https://web.archive.org/web/20141021210320/http://www.royalroadl.com:80/legendary-moonlight-sculptor-volume-3/ ',
        'https://web.archive.org/web/20140805072649/http://www.royalroadl.com/lms-volume-4/',
        'https://web.archive.org/web/20140805062616/http://www.royalroadl.com/lms-volume-5/',
        'https://web.archive.org/web/20140805092033/http://www.royalroadl.com/lms-volume-6/',
        'https://web.archive.org/web/20140805080804/http://www.royalroadl.com/lms-volume-7/',
        'https://web.archive.org/web/20140805084048/http://www.royalroadl.com/lms-volume-8/',
        'https://web.archive.org/web/20140918151907/http://www.royalroadl.com:80/lms-volume-9/',
        'https://web.archive.org/web/20140928193007/http://www.royalroadl.com:80/lms-volume-10/',
        'https://web.archive.org/web/20141019063425/http://www.royalroadl.com:80/lms-volume-11/',
        'https://web.archive.org/web/20141019063715/http://www.royalroadl.com:80/lms-volume-12/',
        'https://web.archive.org/web/20141018052957/http://www.royalroadl.com:80/lms-volume-18/',
        'https://web.archive.org/web/20141022092406/http://www.royalroadl.com:80/lms-volume-20/'] # div 'class':'post-content'
URLs_blogspot = ['http://lmstranslation.blogspot.com.es/p/volume-13-01-05.html',
        'http://lmstranslation.blogspot.com.es/p/1306_17.html',
        'http://lmstranslation.blogspot.com.es/p/1307nov-8.html',
        'http://lmstranslation.blogspot.com.es/p/1308.html',
        'http://lmstranslation.blogspot.com.es/p/1309.html'] #el volumen 13, capitulos 1-5, 6, 7, 8 y 9 div 'class':'post-body entry-content'
URLs_japtem = 'http://japtem.com/lms-volume-14-chapter-1/' #modificar el volumen y el capitulo, volumen 14-17 caps 1-10  div 'class':'post-content'
URLs_vol19 = 'https://web.archive.org/web/20141024012053/http://www.royalroadl.com:80/volume-19-chapter-1/' #cambiar el numero de chapter   div 'class':'post-content'


if not os.path.exists("Volumes"):
    os.makedirs("Volumes")

#Volumenes que estaban completos en la Wayback Machine
for link in enumerate(URLs_royalroadl):
    URL = link[1]
    req = requests.get(URL)
    status_code = req.status_code
    if status_code == 200:
        html = BeautifulSoup(req.text, "html5lib")
        title = html.find('h3', {'class': 'post-title'}).getText()
        file = open("Volumes/"+title, 'w');
        chapter = html.find('div', {'class':'post-content'})
        file.write(chapter.getText().encode("utf-8")+"\n")
        #ps = chapter.find_all(["p","h1", "h2", "h3", "h4", "h5", "h6","table"])
        #for p in enumerate(ps):
            #file.write(p[1].getText().encode("utf-8")+"\n")
        file.close()
    else:
        print "Status Code %d" % status_code
#Volumen 13, en un blogspot, fragmentado
file = open("Volumes/Legendary Moonlight Sculptor Volume 13", 'w');
for link in enumerate(URLs_blogspot):
    URL = link[1]
    req = requests.get(URL)
    status_code = req.status_code
    if status_code == 200:
        html = BeautifulSoup(req.text, "html5lib")
        chapter = html.find('div', {'class':'post-body entry-content'})
        #ps = chapter.find_all(["p","h1", "h2", "h3", "h4", "h5", "h6"])
        file.write(chapter.getText().encode("utf-8")+"\n")
        #for p in enumerate(ps):
            #file.write(p[1].getText().encode("utf-8")+"\n")
        #["p","h1", "h2", "h3", "h4", "h5", "h6"]
    else:
        print "Status Code %d" % status_code
file.close()
#Volumenes 14-17 en japtem, fragmentados
for i in range(14,18):
    file = open("Volumes/Legendary Moonlight Sculptor Volume "+str(i), 'w');
    for j in range(1,11):
        URL = "http://japtem.com/lms-volume-" + str(i) + "-chapter-" + str(j) + "/"
        req = requests.get(URL)
        status_code = req.status_code
        if status_code == 200:
            html = BeautifulSoup(req.text, "html5lib")
            chapter = html.find('div', {'class':'post-content'})
            file.write(chapter.getText().encode("utf-8")+"\n")
        else:
            print "Status Code %d" % status_code
    file.close()
#Volumenes 19 en WaybackMachine, fragmentado
file = open("Volumes/Legendary Moonlight Sculptor Volume 19", 'w');
for j in range(1,11):
    URL = "https://web.archive.org/web/20141024012053/http://www.royalroadl.com:80/volume-19-chapter-"+ str(j) + "/"
    req = requests.get(URL)
    status_code = req.status_code
    if status_code == 200:
        html = BeautifulSoup(req.text, "html5lib")
        chapter = html.find('div', {'class':'post-content'})
        file.write(chapter.getText().encode("utf-8")+"\n")
    else:
        print "Status Code %d" % status_code
file.close()
