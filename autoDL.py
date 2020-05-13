#!/usr/bin/env python3
from selenium import webdriver
import os
import time


DLdir = "path to your designated download directory"
path = os.getcwd() + "/chromedriver"  # This is the path to where you store the drive
topics = ["Introduction", "Amplifiers"]  # This list needs to be modified for the target topics before execution

def isDL():
    files = os.listdir(DLdir)
    for file in files:
        if ".crdownload" in file:
            return 1

    return 0

# Loading the driver for Chrome. The driver should be in the same directory with this script
# TODO: turn PDF viewer off so it downloads instead
# Verify the designated download directory
if not os.path.exists(DLdir):
    os.makedirs(DLdir)

options = webdriver.ChromeOptions()
prefs = {"download.default_directory": DLdir}
options.add_experimental_option("prefs", prefs)
driver = webdriver.Chrome(executable_path=path, options=options)

# Opening ENSC225 website and then log in with "confidential" username and password
driver.get("https://cas.sfu.ca/cas/login?service=https%3a%2f%2fwww.sfu.ca%3a443%2f%7esyrzycki%2f225%2f&allow=apache&message=Enter%20login%20information%20for%20ENSC%20225")
driver.find_element_by_id("username").send_keys("ENSC225")
driver.find_element_by_id("password").send_keys("*********")  # Sorry the password has to be kept confidential
driver.find_element_by_name("submit").click()

i = 0
for topic in topics:
    # Spot the links for target files
    # There should be two links and the 1st should be the lecture note and the 2nd is a hyperlink to .mov files
    # This script aims to download the .mov files as these require tedious clicks
    links = driver.find_elements_by_partial_link_text(topic)
    links[1].click()  # Enter the topic page

    time.sleep(3)
    targetIndex = "0" + str(i)  # .mov file names begin with numbering such as 00, 01 so this gets that string
    i += 1
    targets = driver.find_elements_by_partial_link_text(targetIndex)  # Spot all the .mov files and download them

    for item in targets:
        item.click()

    driver.execute_script("history.back();")  # Go back to the main page and download the next topic

wt = 0
while 1:
    if isDL():
        time.sleep(1)
        wt+=1
    else:
        break

driver.quit()




