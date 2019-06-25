#https://github.com/kaihami/DataMiningLattes/blob/master/Open_Lattes.py

import requests
from bs4 import BeautifulSoup
from PIL import Image
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import pytesseract
import cv2
from time import sleep
import os
import re
import numpy as np



def solve_captcha(url):
    driver = webdriver.Firefox()
    passed = False
    while not passed:

        page = driver.get(url)
        sleep(2)
        driver.save_screenshot("screen.png")
        img = cv2.imread("screen.png", 0)
        captcha = img[295:335, 505:650]
        ret,thresh = cv2.threshold(captcha,225,255,cv2.THRESH_BINARY_INV)
        cv2.imwrite("captcha.png", thresh)
        sleep(1)
        os.system("d:\\tesseract\\tesseract captcha.png output -l captcha")
        output = open("output.txt", "r").read().replace("\n", "").replace(" ", "")
        output = re.sub('[^0-9a-zA-Z]+', '', output).strip()
        cv2.imwrite("captchas\\original\\" + str(output)+".png", captcha)
        cv2.imwrite("captchas\\" + str(output)+".png", thresh)
        output = output[-4:]
        print("captcha:",output, len(output))
        captcha_form = "/html/body/form/div/div/div/div/div/div/div/input"
        fill_path = driver.find_element_by_xpath(captcha_form)
        sleep(1.1)
        for letter in output:
            fill_path.send_keys(letter)
            sleep(.3)
        fill_path.send_keys(Keys.RETURN)
        sleep(5)
        try:
            t = "/html/body/div[3]"
            ok = driver.find_element_by_xpath(t)
            passed = True
            cv2.imwrite("captchas\\success\\" + str(output)+".png", thresh)
            if len(str(driver.page_source)) > 100:
                try:
                    with open("CVs\\"+str(url.split('/')[-1])+".html", "w+" ,errors="ignore") as f:
                        f.write(str(driver.page_source))
                    driver.close()
                except Exception as e:
                    print(e)
        except:
            sleep(5)


if __name__ == "__main__":
    urls = ['http://lattes.cnpq.br/0118224405460667', 'http://lattes.cnpq.br/0167581436112139', 'http://lattes.cnpq.br/0192715697891274', 'http://lattes.cnpq.br/0683060368138422', 'http://lattes.cnpq.br/0950965556955470', 'http://lattes.cnpq.br/0982289255520210', 'http://lattes.cnpq.br/1512576316406197', 'http://lattes.cnpq.br/1739997490142452', 'http://lattes.cnpq.br/1863175020067147', 'http://lattes.cnpq.br/1959285307720446', 'http://lattes.cnpq.br/2190849183511530', 'http://lattes.cnpq.br/2338841032640543', 'http://lattes.cnpq.br/2465553753502316', 'http://lattes.cnpq.br/3086288257972856', 'http://lattes.cnpq.br/3234356076237014', 'http://lattes.cnpq.br/3251775617012106', 'http://lattes.cnpq.br/3579290766137836', 'http://lattes.cnpq.br/3648952311886499', 'http://lattes.cnpq.br/3748302988128047', 'http://lattes.cnpq.br/3818385640376862', 'http://lattes.cnpq.br/3823772604133067', 'http://lattes.cnpq.br/3973077511904385', 'http://lattes.cnpq.br/4031770197674534', 'http://lattes.cnpq.br/4115626573281821', 'http://lattes.cnpq.br/4180982601229727', 'http://lattes.cnpq.br/4620227627509693', 'http://lattes.cnpq.br/4674017654568180', 'http://lattes.cnpq.br/4830529654070227', 'http://lattes.cnpq.br/5054703666891291', 'http://lattes.cnpq.br/5280610737740095', 'http://lattes.cnpq.br/5309315072574421', 'http://lattes.cnpq.br/5701925275743346', 'http://lattes.cnpq.br/5823662263613939', 'http://lattes.cnpq.br/6552120101074110', 'http://lattes.cnpq.br/7017802459850019', 'http://lattes.cnpq.br/7298637758046404', 'http://lattes.cnpq.br/7883906947985490', 'http://lattes.cnpq.br/8145269117998909', 'http://lattes.cnpq.br/8536808087464212', 'http://lattes.cnpq.br/9103911570385178', 'http://lattes.cnpq.br/9107895746529145', 'http://lattes.cnpq.br/9121073346944517', 'http://lattes.cnpq.br/9153211954743941', 'http://lattes.cnpq.br/9696422050573770', 'http://lattes.cnpq.br/9754410711541612']

    exist_cv = ['http://lattes.cnpq.br/'+file[:-5] for file in os.listdir('CVs//')]
    urls2 = [x for x in urls if x not in exist_cv]
    print("pages to download:",len(urls),len(exist_cv),len(urls2))
    for url in urls2:
        print("tentando",url)
        try:
            solve_captcha(url)
        except Exception as e:
            print(e)
