import os
import requests
from flask import Flask, render_template
import urllib3.request
from bs4 import BeautifulSoup
import re
from selenium import webdriver 
from selenium.webdriver.common.keys import Keys 
from selenium.webdriver.chrome.options import Options
import time

''' 
IMPORTANT!!! MUST READ!!! PLEASE VIEW THE INSTRUCTIONS FOR RUNNING TEXT FILE
IN ORDER TO PROPERLY EXECUTE ALL THE CODE. THANK YOU
'''

#required setup line to start creating a flask app
app = Flask(__name__)

#route for home page
@app.route("/")
@app.route("/home")
def home():

    '''
    takes no input
    returns the webpage with the rendertemplate
    links to a html render template and acesses html code to display on page
    '''

    def doorDash():

        #url of the doordash page we want to scrape 
        url = "https://www.doordash.com/store/mcdonald-s-dublin-653741/en-US"
    
        # initiating a headless instance of chrome which goes to our specified url
        options = Options()
        options.headless = True 
        driver = webdriver.Chrome(chrome_options=options)  
        driver.get(url)  
        
        # this is just to ensure that the page is loaded 
        time.sleep(5)  

        # this renders the JS code and stores all of the information in static HTML code. 
        html = driver.page_source 
        
        # Now, we could simply apply bs4 to html variable 
        soup = BeautifulSoup(html, "html.parser") 
        info = soup.find("div", attrs= {"data-item-id":"301278814"})
        infoTwo = info.find("button", class_="sc-imDdex ioWuAb")
        infoTwo = infoTwo.prettify()
        stop = False
        price = ""
        i = 0

        #simple loop extracts our info from the code
        while stop == False:
            if (infoTwo[20+i] == '"'):
                print(price)
                stop = True
            else:
                price += infoTwo[20+i]
                i+=1

        # closing the webdriver
        driver.close() 
        return str(price)

    def uberEats():

        #url of the ubereats page we want to scrape 
        url = "https://www.ubereats.com/san-francisco/food-delivery/mcdonalds-dublin-ave/83609pfuS5CCX0AAmJfNAw?pl=JTdCJTIyYWRkcmVzcyUyMiUzQSUyMkR1YmxpbiUyMiUyQyUyMnJlZmVyZW5jZSUyMiUzQSUyMkNoSUpsWkpJelNIc2o0QVJyeTRoWFRyYkIzOCUyMiUyQyUyMnJlZmVyZW5jZVR5cGUlMjIlM0ElMjJnb29nbGVfcGxhY2VzJTIyJTJDJTIybGF0aXR1ZGUlMjIlM0EzNy43MjAyNDYzJTJDJTIybG9uZ2l0dWRlJTIyJTNBLTEyMS44Njc2NDY0JTdE"
    
        # initiating a headless instance of chrome which goes to our specified url
        options = Options()
        options.headless = True 
        driver = webdriver.Chrome(chrome_options=options)  
        driver.get(url)  
        
        # this is just to ensure that the page is loaded 
        time.sleep(10) 

        # this renders the JS code and stores all of the information in static HTML code. 
        html = driver.page_source 
        
        # Now, we could simply apply bs4 to html variable 
        soup = BeautifulSoup(html, "html.parser") 
        infoTwo = soup.find("div", class_="cc c6 c7 ag")
        infoTwo = infoTwo.prettify()
        stop = False
        price = ""
        i = 0       

        #simple loop extracts our info from the code
        while stop == False:
            if (infoTwo[25+i] == '<'):
                print(price)
                stop = True
            else:
                price += infoTwo[25+i]
                i+=1

        # closing the webdriver
        driver.close() 
        return str(price)

    def grubHub():

        #url of the grubhub page we want to scrape 
        url = "https://www.grubhub.com/food/mcdonalds/menu"
    
        # initiating a headless instance of chrome which goes to our specified url
        options = Options()
        options.headless = True 
        driver = webdriver.Chrome(chrome_options=options)  
        driver.get(url)  
        
        # this is just to ensure that the page is loaded 
        time.sleep(5)  

        # this renders the JS code and stores all of the information in static HTML code. 
        html = driver.page_source 
        
        # Now, we could simply apply bs4 to html variable 
        soup = BeautifulSoup(html, "html.parser") 
        info = soup.find("div", attrs = {"id":"menuItem-1806142594"})
        infoTwo = info.find("span", class_="menuItem-displayPrice")
        infoTwo = infoTwo.prettify()
        stop = False
        price = ""
        i = 0

        #simple loop extracts our info from the code
        while stop == False:
            if (infoTwo[83+i] == '<'):
                print(price)
                stop = True
            else:
                price += infoTwo[83+i]
                i+=1

        # closing the webdriver
        driver.close() 
        return str(price)
    
    #launches the web app and sends variables to html 
    door = doorDash();
    uber = uberEats();
    grub = grubHub();
    return render_template('index.html', door = door, uber = uber, grub = grub)
