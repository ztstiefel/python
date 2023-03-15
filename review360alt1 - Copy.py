# Imports

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Global Variables

options = Options()
options.headless = True

# Opens the chrome windows (GUI/Headless)

driver = webdriver.Chrome(options=options)

# This function opens the Review360 login page, enters the user's email address, and continues

def Review360Login():
    driver.implicitly_wait(5)
    driver.get('https://www.psiwaresolution.com/Review360/Login')
    assert 'Review360' in driver.title
    elem1 = driver.find_element(By.NAME, 'EmailAddress')
    elem1.clear()
    elem1.send_keys('<EMAIL_ADDRESS>')
    elem1.send_keys(Keys.RETURN)

Review360Login()

# Use this for headless mode

def GoogleAuth01():
    driver.implicitly_wait(5)
    elem2 = driver.find_element(By.XPATH, '/html/body/div/div[2]/div[2]/div[1]/form/div/div/div/div/div/input[1]')
    elem2.clear()
    elem2.send_keys('<EMAIL_ADDRESS>')
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
    checkbox = driver.find_element(By.ID, 'svisr_1385416_2')
    checkbox.click()

    checkbox = driver.find_element(By.ID, 'svisr_1385406_2')
    checkbox.click()

    checkbox = driver.find_element(By.ID, 'svisr_1385407_2')
    checkbox.click()

    checkbox = driver.find_element(By.ID, 'svisr_1385415_2')
    checkbox.click()

Student01Scoring()

# Selects (period 3) objective scoring box 1

def objective_scoring01a():
    checkbox = driver.find_element(By.ID, 'svo_5426084_2')
    checkbox.click()

objective_scoring01a()

# Selects (period 3) objective scoring popup 1

def objective_scoring01b():
    checkbox = driver.find_element(By.ID, 'ObjectivePointsPopup')
    checkbox.click()

objective_scoring01a()

# Selects (period 3) 'Full Points'

driver.find_element(By.XPATH, '//*[@id="ObjectivePointsPopup"]/div/div/div[3]').click()

# Save changes, close browser windows, then exit the webdriver

driver.find_element(By.ID, 'SaveBTN').click()
driver.close()
driver.quit()