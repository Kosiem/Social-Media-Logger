import configparser as cp
from selenium import webdriver

userEnv = cp.ConfigParser()
userEnv.read("userEnv.cfg")

# Function to read specified browser in config file
def CheckBrowser():

    browser = userEnv.get("Browser", "name")

    if browser == "Google Chrome":
        return "Google Chrome"
    elif browser == "Mozilla Firefox":
        return "Mozilla Firefox"
    elif browser == "Microsoft Edge":
        return "Microsoft Edge"
    else:
        raise ValueError("Browser not supported")

# Function to fetch username, password and url of page from config file
def getPasses(socialMedia):
    for media in userEnv.sections():
        if socialMedia == media:
            url = userEnv.get(socialMedia, "url")
            username = userEnv.get(socialMedia, "email")
            password = userEnv.get(socialMedia, "password")
            return url, username, password
    else:
        raise ValueError("No matching social media name")

