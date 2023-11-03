from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
import ConfigHandling

# Get passes from config file
passes = ConfigHandling.getPasses("Facebook")
url = passes[0]
username = passes[1]
password = passes[2]

# Function responsible for login, and opening browser in correct mode
def LogInFacebook():

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

    # Accept necessary cookies
    cookie_button = WebDriverWait(driver, 10).until(ec.presence_of_element_located((By.XPATH, "//button[@data-cookiebanner='accept_button']")))
    cookie_button.click()

    # Wait for form to load, pass login, password, and press login button
    WebDriverWait(driver, 10).until(ec.presence_of_element_located((By.XPATH, "//input[@name='email' and @id='email']")))
    driver.find_element(By.XPATH, "//input[@name='email' and @id='email']").send_keys(username)
    driver.find_element(By.XPATH, "//input[@type='password' and @name='pass' and @id='pass']").send_keys(password)
    driver.find_element(By.XPATH, "//button[@type='submit' and @name='login']").click()






