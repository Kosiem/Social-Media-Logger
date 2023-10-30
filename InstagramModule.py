from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
import ConfigHandling

passes = ConfigHandling.getPasses("Instagram")
username = passes[1]
url = passes[0]
print(url)
password = passes[2]
def LogInInstagram():

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

    cookie_button = WebDriverWait(driver,10).until(ec.presence_of_element_located((By.XPATH, "//button[@class='_a9-- _a9_0']")))
    cookie_button.click()

    login = WebDriverWait(driver,10).until(ec.presence_of_element_located((By.XPATH, "//input[@name='username']")))
    login.send_keys(username)

    driver.find_element(By.XPATH, "//input[@type='password' and @name='password']").send_keys(password)
    driver.find_element(By.XPATH, "//button[@class = '_acan _acap _acas _aj1-']").click()




