# This script is used to automate daily data collection for the Review360 data entry system. 
# At the moment it is highly specific/brittle and may break as each student's scoring page is updated

# If this script fails immediately, be sure to check for the latest ChromeDriver: 
# https://chromedriver.chromium.org/downloads to download and install the latest version
# that matches the installed version of Chrome.

# ToDo:
# Add ability to request for user input for email address and password.
# Add/change ability to scrape and display the students in Review360.
# Add/change ability/flexibility to scrape and display which strategies need to be checked, and check them off accordingly.
# Add/change ability to scrape and display objectives for user input.
# Figure out how to package this script with either a GUI, Docker, or Web Service.
# Figure out if this script can be hosted on a headless system (server) and still function.

# Imports

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd # Not sure if necessary, don't feel like checking right now.

# User Input for Student Objective 1

def User_Input01():

    objective01 = input('''
    "<TEXT_REDACTED>"
    
    Please type 'yes', 'no', or 'skip'.''').lower()

    return objective01

# User Input for Student Objective 2

def User_Input02():

    objective02 = input('''
    "<TEXT_REDACTED>"

    Please type 'yes', 'no', or 'skip'.''').lower()
    
    return objective02

# User Input for Student Objective 3

def User_Input03():

    objective03 = input('''
    "<TEXT_REDACTED>"
    
    Please type 'yes', 'no', or 'skip'.''').lower()
    
    return objective03

# Global Variables

options = Options()
options.headless = True

User_Input01a = User_Input01()
User_Input02a = User_Input02()
User_Input03a = User_Input03()

# Sanity Check for user input responses

print(User_Input01a, User_Input02a, User_Input03a)

# Opens the chrome windows (GUI/Headless)

driver = webdriver.Chrome(options=options)

# This function opens the Review360 login page, enters the user's email address, and continues

def Review360Login():
    driver.implicitly_wait(5)
    driver.get('https://www.psiwaresolution.com/Review360/Login')
    assert 'Review360' in driver.title
    elem1 = driver.find_element(By.NAME, 'EmailAddress')
    elem1.clear()
    elem1.send_keys('<EMAIL>')
    elem1.send_keys(Keys.RETURN)

Review360Login()

# Use this for headless mode

def GoogleAuth01():
    driver.implicitly_wait(5)
    elem2 = driver.find_element(By.XPATH, '/html/body/div/div[2]/div[2]/div[1]/form/div/div/div/div/div/input[1]')
    elem2.clear()
    elem2.send_keys('<EMAIL>')
    elem2.send_keys(Keys.RETURN)

GoogleAuth01()

# Use this for headless mode

def GoogleAuth02():
    driver.implicitly_wait(5)
    elem3 = driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/div/div[2]/form/span/div/div[2]/input')
    elem3.clear()
    elem3.send_keys('<PASSWORD>')
    elem3.send_keys(Keys.RETURN)

GoogleAuth02()

# This function selects a student and opens their scoring page in a new tab

def OpenStudentTab01():
    assert 'Review360' in driver.title
    element = WebDriverWait(driver, 5).until(
        EC.presence_of_element_located((By.PARTIAL_LINK_TEXT, '<STU_LN>, <STU_FN>'))
        )
    element.send_keys(Keys.CONTROL + Keys.RETURN)

OpenStudentTab01()

# Switch to scoring tab and select 'score' link

def Student01Select():
    driver.switch_to.window(driver.window_handles[1])
    link = driver.find_element(By.PARTIAL_LINK_TEXT, 'Score' )
    link.click()

Student01Select()

#Select strategy implementation checkboxes Strategies

def Student01Scoring():
    checkbox = driver.find_element(By.ID, 'svisr_1331214_2')
    checkbox.click()

    checkbox = driver.find_element(By.ID, 'svisr_1331215_2')
    checkbox.click()

    checkbox = driver.find_element(By.ID, 'svisr_1331216_2')
    checkbox.click()

    checkbox = driver.find_element(By.ID, 'svisr_1331193_2')
    checkbox.click()

    checkbox = driver.find_element(By.ID, 'svisr_1331191_2')
    checkbox.click()

    checkbox = driver.find_element(By.ID, 'svisr_1331212_2')
    checkbox.click()

Student01Scoring()

# Selects (period 3) objective scoring box 1

def objective_scoring01a():
    checkbox = driver.find_element(By.ID, 'svo_5267610_2')
    checkbox.click()

objective_scoring01a()

# Selects (period 3) objective scoring popup 1

def objective_scoring01b():
    checkbox = driver.find_element(By.ID, 'ObjectivePointsPopup')
    checkbox.click()

objective_scoring01a()

# Selects (period 3) 'Not Scored, 'No Points', or 'Full Points' based on user input for objective scoring popup 1

def objective_scoring01c():
    if User_Input01a == 'skip':
        driver.find_element(By.XPATH, '//*[@id="ObjectivePointsPopup"]/div/div/div[1]').click()
    if User_Input01a == 'no':
        driver.find_element(By.XPATH, '//*[@id="ObjectivePointsPopup"]/div/div/div[2]').click()
    if User_Input01a == 'yes':
        driver.find_element(By.XPATH, '//*[@id="ObjectivePointsPopup"]/div/div/div[3]').click()

objective_scoring01c()

# Selects (period 3) objective scoring box 2

def objective_scoring02a():
    checkbox = driver.find_element(By.ID, 'svo_5267609_2')
    checkbox.click()

objective_scoring02a()

# Selects (period 3) objective scoring popup 2

def objective_scoring02b():
    checkbox = driver.find_element(By.ID, 'ObjectivePointsPopup')
    checkbox.click()

objective_scoring02a()

# Selects (period 3) 'Not Scored, 'No Points', or 'Full Points' based on user input for objective scoring popup 2

def objective_scoring02c():
    if User_Input02a == 'skip':
        driver.find_element(By.XPATH, '//*[@id="ObjectivePointsPopup"]/div/div/div[1]').click()
    if User_Input02a == 'no':
        driver.find_element(By.XPATH, '//*[@id="ObjectivePointsPopup"]/div/div/div[2]').click()
    if User_Input02a == 'yes':
        driver.find_element(By.XPATH, '//*[@id="ObjectivePointsPopup"]/div/div/div[3]').click()

objective_scoring02c()

# Selects (period 3) objective scoring box 2

def objective_scoring03a():
    checkbox = driver.find_element(By.ID, 'svo_5267608_2')
    checkbox.click()

objective_scoring03a()

# Selects (period 3) objective scoring popup 3

def objective_scoring03b():
    checkbox = driver.find_element(By.ID, 'ObjectivePointsPopup')
    checkbox.click()

objective_scoring03a()

# Selects (period 3) 'Not Scored, 'No Points', or 'Full Points' based on user input for objective scoring popup 3

def objective_scoring03c():
    if User_Input03a == 'skip':
        driver.find_element(By.XPATH, '//*[@id="ObjectivePointsPopup"]/div/div/div[1]').click()
    if User_Input03a == 'no':
        driver.find_element(By.XPATH, '//*[@id="ObjectivePointsPopup"]/div/div/div[2]').click()
    if User_Input03a == 'yes':
        driver.find_element(By.XPATH, '//*[@id="ObjectivePointsPopup"]/div/div/div[3]').click()

objective_scoring03c()

# Save changes, close browser windows, then exit the webdriver

driver.find_element(By.ID, 'SaveBTN').click()
driver.close()
driver.quit()