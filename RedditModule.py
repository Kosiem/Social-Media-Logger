import time
from selenium.webdriver.common.action_chains import ActionChains
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as ec
import ConfigHandling

# Get passes from config file
passes = ConfigHandling.getPasses("Reddit")
url = passes[0]
username = passes[1]
password = passes[2]

# Function responsible for login, and opening browser in correct mode
def LogInReddit():

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

    # Wait for login button to load and press it
    login_button = WebDriverWait(driver,10).until(ec.presence_of_element_located((By.XPATH, "//a[@href='https://www.reddit.com/login']")))
    login_button.click()

    # Pass username, password and press enter to login
    user = WebDriverWait(driver, 10).until(ec.presence_of_element_located((By.XPATH, "//span[@slot='login-username']/input[@name='username']")))
    user.send_keys(username)
    driver.find_element(By.XPATH, "//span[@slot='login-password']/input[@name='password']").send_keys(password)
    keyboard = ActionChains(driver)
    keyboard.send_keys(Keys.ENTER).perform()
