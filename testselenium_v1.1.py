#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct  3 13:59:06 2019

@author: dubiez
"""

# Librairies pour selenuim
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from requests import get
from requests.exceptions import RequestException
from contextlib import closing

#~ import creds
import os,configparser # credentials: 

#Lien de l'url
url = "https://www.fun-mooc.fr/"

#set webdriver path
driver = webdriver.Firefox(executable_path ='/home/dubiez/anaconda3/lib/python3.7/site-packages/selenium/webdriver/geckodriver-v0.24.0-linux64/geckodriver')

# Fonction de la connection

def simple_get(url):
    """
    Se connecte a l'url, si statut = 200 retourne le contenu ( en appelant is_good_response)
    """
    try:
        with closing(get(url, stream=True)) as resp:
            if is_good_response(resp):
                return resp.content
            else:
                return None

    except RequestException as e:
        log_error('Error during requests to {0} : {1}'.format(url, str(e)))
        return None
def is_good_response(resp):
    """
    Renvoie 200 si connection a l'url
    """
    content_type = resp.headers['Content-Type'].lower()
    return (resp.status_code == 200 
            and content_type is not None 
            and content_type.find('html') > -1)
def log_error(e):
    """
    retourne l'erreur
    """
    print(e)

driver.get(url)

login=driver.find_element_by_css_selector('.login-link').click() 

# email mot de passe mooc

config = configparser.ConfigParser()
login = config.read_file(open(os.path.expanduser("~/.datalab.cnf")))
config['mooc']['user']  

driver.find_element_by_name("submit").click()


driver.find_element_by_name('email').send_keys(config['mooc']['user'] )
driver.find_element_by_name('password').send_keys(config['mooc']['password'])
driver.find_element_by_name('loginbutton').click()