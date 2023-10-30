from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.action_chains import ActionChains
import ConfigHandling

passes = ConfigHandling.getPasses("TikTok")
username = passes[1]
url = passes[0]
print(url)
password = passes[2]
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

    driver.get(url)
    driver.maximize_window()

    mouse = ActionChains(driver)

    WebDriverWait(driver, 10).until(ec.presence_of_element_located((By.XPATH, "//button[@id='header-login-button' and @data-e2e='top-login-button']")))
    mouse.move_to_element(driver.find_element(By.XPATH, "//button[@id='header-login-button']")).perform()
    mouse.click().perform()

    choose_login = WebDriverWait(driver, 10).until(ec.presence_of_element_located((By.XPATH, "//div[@class='tiktok-15cgryv-DivBoxContainer e1cgu1qo0']")))
    choose_login.click()

    choose_email = WebDriverWait(driver, 10).until(ec.presence_of_element_located((By.XPATH, "//a[@href='/login/phone-or-email/email']")))
    choose_email.click()

    login = WebDriverWait(driver, 10).until(ec.presence_of_element_located((By.XPATH, "//input[@name='username']")))
    login.send_keys(username)
    driver.find_element(By.XPATH, "//input[@type='password']").send_keys(password)

    submit = WebDriverWait(driver, 10).until(ec.visibility_of_element_located((By.XPATH, "//button[@type='submit' and @data-e2e='login-button']")))
    submit.click()
