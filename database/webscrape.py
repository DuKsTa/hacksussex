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

button_xpath = "/html/body/div[1]/div/div/div/div[7]/div[1]"
# Define the base XPaths for the questions and answers containers
insurance_type_xpath = "/html/body/div[1]/div/div/div/div[4]/button[1]"
faq_xpath = "/html/body/div[1]/div/div/div/div[6]/div/button[1]"

home_insurance = "/html/body/div[1]/div/div/div/div[4]/button[2]"
home_insurance_faq = "/html/body/div[1]/div/div/div/div[6]/div[1]"
home_questions = "/html/body/div[1]/div/div/div/div[6]/div[2]/div"

# Locate the container that holds all the buttons
container_xpath = "#__next > div > div > div > div.styles_helpTriageMainButtonContainer__REpR5"
container = driver.find_elements(By.CSS_SELECTOR, container_xpath)

faq = "#__next > div > div > div > div.styles_topFaqWrapper__wCfac > div"
faqs = driver.find_elements(By.CSS_SELECTOR, faq)

""
"#__next > div > div > div > div.styles_topFaqWrapper__wCfac > div.styles_topFaqContainer__n8Ij3"
# questions = "#__next > div > div > div > div.styles_topFaqWrapper__wCfac > div.styles_resultsContainer__mpVop"
# question = driver.find_element(By.CSS_SELECTOR, questions)

# Main page
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
        # button = driver.find_elements(By.TAG_NAME, "button")
        # print(f"Length of it is {len(button)}")
        button = driver.find_elements(By.XPATH, "//*[@id='__next']/div/div/div/div[6]/div[1]/button")
        for t in button:
            t.click()
            questions = driver.find_elements(By.XPATH, "//*[@id='__next']/div/div/div/div[6]/div[2]/div")
            print(f"Length of divs are {len(questions)}")   
            for div in questions:
                buttons = driver.find_elements(By.TAG_NAME, "button")
                for butt in buttons:
                    print(div)

        # for t in button:
        #     t.click()

    
# for i in container:
#     print(i)

# Find all the button elements within the container
# buttons = container.find_elements(By.TAG_NAME, 'button')
# faq = container.find_elements(By.XPATH, home_insurance_faq)

# # Click each button
# for button in buttons:
#     button.click()
#     for i in faq:
#         print(i)

# butt = "/html/body/div[1]/div/div/div/div[6]/div[2]/div/div[2]/div/div/p[1]"

# buttons_text = driver.find_element(By.XPATH, butt)

# print(buttons_text.text)

# # Loop through each <p> element and extract the text
# for p in paragraphs:
#     print(p)
#     text = p.text
#     # Process the text as needed, such as printing or saving to a file
#     print(text)

# Close the driver when done
driver.quit()