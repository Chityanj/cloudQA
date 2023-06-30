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


# Regex pattern
dob_pattern = dob_input.get_attribute("pattern")

# Test Case 3: Enter a valid date
date = "1999-05-30"
dob_input.clear()
dob_input.send_keys(date)
dob_input.send_keys(Keys.ENTER) # Check using ENTER key
time.sleep(2)

dob_match = bool(re.match(dob_pattern, date))
if dob_match:
    print(f'Test passed! {date} is a valid date.')
else:
    print(f'Test failed! {date} is not a valid date.')


# Test Case 4: Enter an invalid date
date = "1999-13-45"  # Invalid month and day
dob_input.clear()
dob_input.send_keys(date)
dob_input.send_keys(Keys.ENTER)
dob_match = bool(re.match(dob_pattern, date))
if dob_match:
    print(f'Test passed! {date} is a valid date.')
else:
    print(f'Test failed! {date} is not a valid date.')

# Test Case 5: Submit the form (assuming it exists)

# Wait for a few seconds to see the result

time.sleep(10)
# Quit the browser
driver.quit()