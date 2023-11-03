from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
import ConfigHandling

# Get passes from config file
passes = ConfigHandling.getPasses("LinkedIn")
url = passes[0]
username = passes[1]
password = passes[2]

# Function responsible for login, and opening browser in correct mode
def LogInLinkedIn():

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

    # Wait for form to load, pass login, password and press login button
    login = WebDriverWait(driver,10).until(ec.presence_of_element_located((By.XPATH, "//input[@id='session_key']")))
    login.send_keys(username)
    driver.find_element(By.XPATH, "//input[@id='session_password']").send_keys(password)
    driver.find_element(By.XPATH, "//div[@data-id='sign-in-form__footer']/button").click()