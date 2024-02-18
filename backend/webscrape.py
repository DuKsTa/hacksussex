from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Setup WebDriver
service = Service(executable_path='/opt/homebrew/bin/chromedriver')  # Update this path
driver = webdriver.Chrome(service=service)
wait = WebDriverWait(driver, 10)

# Open the website
driver.get("https://www.hastingsdirect.com/help/")  # Replace with the actual URL

# Wait for the page to load
time.sleep(5)

# Locate the container that holds all the buttons
container_xpath = "#__next > div > div > div > div.styles_helpTriageMainButtonContainer__REpR5"
container = driver.find_elements(By.CSS_SELECTOR, container_xpath)

faq = "#__next > div > div > div > div.styles_topFaqWrapper__wCfac > div"
faqs = driver.find_elements(By.CSS_SELECTOR, faq)

# questions = "#__next > div > div > div > div.styles_topFaqWrapper__wCfac > div.styles_resultsContainer__mpVop"
# question = driver.find_element(By.CSS_SELECTOR, questions)
question = ""
# Main page
with open('data_scraping.txt', 'w') as f:
    for i in container:
        # click on the insurances
        i.click()
        buttons = driver.find_elements(By.TAG_NAME, "button")
        for index, b in enumerate(buttons):
            # If it's the car insurance then skip
            if index == 0:
                continue
            # Select the insurances
            b.click()
            button = driver.find_elements(By.XPATH, "//*[@id='__next']/div/div/div/div[6]/div[1]/button")
            for t in button:
                t.click()
                time.sleep(1)
                questions = driver.find_elements(By.XPATH, "//*[@id='__next']/div/div/div/div[6]/div[2]/div//*")
                time.sleep(0.1)
                print(f"Length of divs are {len(questions)}")
                for q in questions:
                    if len(q.text) < 5:
                        continue
                    if question == q.text.strip():
                        continue
                    question = q.text.strip()
                    print(q.accessible_name)
                    f.write(f'Question:{question}\n')
    
driver.quit()