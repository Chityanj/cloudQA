from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
import time
import re

driver = webdriver.Chrome("/home/chityanj/linkedin/scrape/chromedriver")
driver.get("https://app.cloudqa.io/home/AutomationPracticeForm")
time.sleep(5)

# Element Selectors
dob_input = driver.find_element_by_css_selector("input#dob.form-control") # DOB field
mob_input = driver.find_element_by_css_selector("input#mobile.form-control") # Mobile field
name_input = driver.find_element_by_css_selector("input#fname.form-control") # Name field


# Regex pattern
dob_pattern = dob_input.get_attribute("pattern")
mob_pattern = mob_input.get_attribute("pattern")



# DOB Test Cases
date = "1999-05-30"
dob_input.clear()
dob_input.send_keys(date)
dob_input.send_keys(Keys.ENTER) # Check using ENTER key
dob_match = bool(re.match(dob_pattern, date))
if dob_match:
    print(f'Test passed! {date} is a valid date.')
else:
    print(f'Test failed! {date} is not a valid date.')

time.sleep(2)
date = "1999-13-45"  # Invalid month and day
dob_input.clear()
dob_input.send_keys(date)
dob_input.send_keys(Keys.ENTER)
dob_match = bool(re.match(dob_pattern, date))
if dob_match:
    print(f'Test passed! {date} is a valid date.')
else:
    print(f'Test failed! {date} is not a valid date.')

time.sleep(2)

# Mobile field test cases

mobile = "1234567890" # 10 digits valid
mob_input.clear()
mob_input.send_keys(mobile)
mob_input.send_keys(Keys.ENTER)
mob_match = bool(re.match(mob_pattern, mobile))
if mob_match:
    print(f'Test passed! {mobile} is a valid mobile number.')
else:
    print(f'Test failed! {mobile} is not a valid mobile number.')

time.sleep(2)

mobile = "123456780" #Invalid mobile number digits
mob_input.clear()
mob_input.send_keys(mobile)
mob_input.send_keys(Keys.ENTER)
mob_match = bool(re.match(mob_pattern, mobile))
if mob_match:
    print(f'Test passed! {mobile} is a valid mobile number.')
else:
    print(f'Test failed! {mobile} is not a valid mobile number.')

time.sleep(2)

# Name field test cases
name = "John Doe" # Valid name
name_input.clear()
name_input.send_keys(name)
name_input.send_keys(Keys.ENTER)
name_match = bool(re.match("^[a-zA-Z ]*$", name))
if name_match:
    print(f'Test passed! {name} is a valid name.')
else:
    print(f'Test failed! {name} is not a valid name.')

time.sleep(2)

name = "John Doe 123" # Invalid name
name_input.clear()
name_input.send_keys(name)
name_input.send_keys(Keys.ENTER)
name_match = bool(re.match("^[a-zA-Z ]*$", name))
if name_match:
    print(f'Test passed! {name} is a valid name.')
else:
    print(f'Test failed! {name} is not a valid name.')
    



time.sleep(10)
# Quit the browser
driver.quit()