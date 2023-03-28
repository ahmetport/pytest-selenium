from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.maximize_window()
driver.get("https://www.kodlama.io/courses/")
sleep(3)
listOfCourses = driver.find_elements(By.CLASS_NAME,"course-listing")
print(f"Kodlamaio sitesinde şu anda {len(listOfCourses)} adet kurs var.")
# sleep(10)
while True:
    continue
# HTML LOCATORS


# full xpath
# /html/body/div[7]/div/div[11]/div/div[2]/div[2]/div/div/div[1]/div/div/div/div/div/div/div[1]/a

# xpath
# //*[@id="rso"]/div[1]/div/div/div/div/div/div/div[1]/a

# web scraping
# data scraping