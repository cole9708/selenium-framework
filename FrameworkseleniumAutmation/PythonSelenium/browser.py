import webbrowser
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

s= Service('C:\\Users\\cole9\\PycharmProjects//chromedriver.exe')
driver =webdriver.Chrome(service=s)
driver.get('https://www.rahulshettyacademy.com')

#browser =webbrowser
#browser.open('https://www.rahulshettyacademy.com')

