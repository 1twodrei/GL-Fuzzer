#!/usr/bin/python3
from selenium import webdriver
from urllib.parse import quote
from time import sleep
import random

vulnerable_url = 'https://localhost:8085/'

form_class = 'new-note common-note-form gfm-form js-main-target-form'
#input_field_id = './..'
#submit_button_id = './..'
payload_exe = 'js-request:localhost:8123'

driver = webdriver.Safari()
driver.get(vulnerable_url)
sleep(5)
form = driver.find_element_by_class_name("form_class")
#input_field = driver.find_element_by_id(input_field_id)
#submit_button = driver.find_element_by_id(submit_button_id)

def random_payload():
    random_payload_string = ""
    i = 100
    while i >= 0:
        random_payload_string += payload_parameters[random()]
    return random_payload_string

with open('payload-parameters.txt', 'r') as file:
    payload_parameters = [line.strip() for line in file.readlines() if line.strip()]

while(open('payload-parameters.txt', 'r') == ""):
    input_field = form.find_element_by_tag_name("input")
    input_field.send_keys(random_payload())
    #submit_button.click()
    form.submit()





driver.quit()
