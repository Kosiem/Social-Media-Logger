from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.action_chains import ActionChains
import ConfigHandling

# Get passes from config file
passes = ConfigHandling.getPasses("TikTok")
url = passes[0]
username = passes[1]
password = passes[2]

# Function responsible for login, and opening browser in correct mode
def LogInTikTok():

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

    # Wait to element to be loaded, and move mouse to it
    mouse = ActionChains(driver)
    WebDriverWait(driver, 10).until(ec.presence_of_element_located((By.XPATH, "//button[@id='header-login-button' and @data-e2e='top-login-button']")))
    mouse.move_to_element(driver.find_element(By.XPATH, "//button[@id='header-login-button']")).perform()
    mouse.click().perform()

    # In menu choose login option
    choose_login = WebDriverWait(driver, 10).until(ec.presence_of_element_located((By.XPATH, "//div[@class='tiktok-15cgryv-DivBoxContainer e1cgu1qo0']")))
    choose_login.click()

    # Choose option to login by email
    choose_email = WebDriverWait(driver, 10).until(ec.presence_of_element_located((By.XPATH, "//a[@href='/login/phone-or-email/email']")))
    choose_email.click()

    # Wait to load form, and pass login and password here
    login = WebDriverWait(driver, 10).until(ec.presence_of_element_located((By.XPATH, "//input[@name='username']")))
    login.send_keys(username)
    driver.find_element(By.XPATH, "//input[@type='password']").send_keys(password)

    # Wait, after finishing form to submit button become visible, and press it
    submit = WebDriverWait(driver, 10).until(ec.visibility_of_element_located((By.XPATH, "//button[@type='submit' and @data-e2e='login-button']")))
    submit.click()
