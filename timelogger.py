import requests
from requests.auth import HTTPBasicAuth
from configparser import ConfigParser

CONFIG = ConfigParser()
CONFIG.read("config.ini")
URL = "https://extranet.opusvl.com"

username = CONFIG["OpusVL"]["username"]
password = CONFIG["OpusVL"]["password"]
auth = HTTPBasicAuth(username, password)

r = requests.get(URL, verify=False, auth=auth)
print(r.text)
