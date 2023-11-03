import time

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import ConfigHandling

# Get passes from config file

passes = ConfigHandling.getPasses("Youtube")
url = passes[0]
username = passes[1]
password = passes[2]

# Function responsible for login, and opening browser in correct mode
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

    # Open and maximize browser
    driver.get(url)
    driver.maximize_window()

    # Wait for elements to be loaded and then move mouse to it
    mouse = ActionChains(driver)
    WebDriverWait(driver, 10).until(ec.presence_of_element_located((By.XPATH, "//button[@class='yt-spec-button-shape-next yt-spec-button-shape-next--filled yt-spec-button-shape-next--mono yt-spec-button-shape-next--size-m']")))
    mouse.move_to_element_with_offset(driver.find_element(By.XPATH, "//button[@class='yt-spec-button-shape-next yt-spec-button-shape-next--filled yt-spec-button-shape-next--mono yt-spec-button-shape-next--size-m']"), 150, 0).perform
    mouse.click().perform()

    # Wait for elements to be loeaded
    WebDriverWait(driver, 10).until(ec.presence_of_element_located((By.XPATH, "//div[@class='yt-spec-touch-feedback-shape__fill']")))
    time.sleep(2)

    # Click login button
    mouse.move_to_element(driver.find_element(By.XPATH, "//ytd-button-renderer[@id='sign-in-button']")).perform()
    mouse.click().perform()

    # Enter email
    email = WebDriverWait(driver, 10).until(ec.presence_of_element_located((By.XPATH, "//input[@type='email' and @name='identifier']")))
    email.send_keys(username)
    keyboard = ActionChains(driver)
    keyboard.send_keys(Keys.ENTER).perform()

    # Enter password
    password = WebDriverWait(driver, 10).until(ec.presence_of_element_located((By.XPATH, "//input[@type='password' and name='Passwd']")))
    password.send_keys(password)