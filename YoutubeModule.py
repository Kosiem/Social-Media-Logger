import time

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import ConfigHandling

passes = ConfigHandling.getPasses("Youtube")
username = passes[1]
url = passes[0]
print(url)
password = passes[2]
def LogInYoutube():

    if ConfigHandling.CheckBrowser() == "Google Chrome":
        option = webdriver.ChromeOptions()
        option.add_experimental_option("detach", True)
        option.add_argument("--incognito")
        driver = webdriver.Chrome(options=option)
    elif ConfigHandling.CheckBrowser() == "Mozilla Firefox":
        option = webdriver.FirefoxOptions()
        option.add_argument("--private")
        option.add_argument("--detach")
        driver = webdriver.Firefox(options=option)
    elif ConfigHandling.CheckBrowser() == "Microsoft Edge":
        option = webdriver.EdgeOptions()
        option.add_experimental_option("detach", True)
        option.add_argument("--insecure")
        driver = webdriver.Edge(options=option)

    driver.get(url)
    driver.maximize_window()
    mouse = ActionChains(driver)
    WebDriverWait(driver, 10).until(ec.presence_of_element_located((By.XPATH, "//button[@class='yt-spec-button-shape-next yt-spec-button-shape-next--filled yt-spec-button-shape-next--mono yt-spec-button-shape-next--size-m']")))
    mouse.move_to_element_with_offset(driver.find_element(By.XPATH, "//button[@class='yt-spec-button-shape-next yt-spec-button-shape-next--filled yt-spec-button-shape-next--mono yt-spec-button-shape-next--size-m']"), 150, 0).perform
    mouse.click().perform()


    WebDriverWait(driver, 10).until(ec.presence_of_element_located((By.XPATH, "//div[@class='yt-spec-touch-feedback-shape__fill']")))
    time.sleep(2)
    mouse.move_to_element(driver.find_element(By.XPATH, "//ytd-button-renderer[@id='sign-in-button']")).perform()
    mouse.click().perform()

    email = WebDriverWait(driver, 10).until(ec.presence_of_element_located((By.XPATH, "//input[@type='email' and @name='identifier']")))
    email.send_keys(username)

    keyboard = ActionChains(driver)
    keyboard.send_keys(Keys.ENTER).perform()

    password = WebDriverWait(driver, 10).until(ec.presence_of_element_located((By.XPATH, "//input[@type='password' and name='Passwd']")))
    password.send_keys(password)


   # driver.find_element(By.XPATH, "//span[@jsname='V67aGc']").click()
