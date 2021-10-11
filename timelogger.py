import json
import requests
from requests.auth import HTTPBasicAuth
from configparser import ConfigParser


CONFIG = ConfigParser()
CONFIG.read("config.ini")
BASE_URL = "https://extranet.opusvl.com/"

username = CONFIG["opusvl"]["username"]
password = CONFIG["opusvl"]["password"]
auth = HTTPBasicAuth(username, password)


def login() -> requests.Session:
    """Create a session which logs into timelogger"""
    data = {
        "username": username,
        "password": password,
        "remember": "1",
        "submit": "Login",
    }
    session = requests.Session()
    session.post(BASE_URL + "login", verify=False, data=data, auth=auth)
    session.get(BASE_URL, verify=False, auth=auth)
    return session


def log_entry(toggl_data: list) -> None:
    """
    Log entry to time logger using given data.

    Data should be in the format:
    {
        'contract': <str>,
        'description': <str>,
        'time_spent_seconds': <int>,
        'date': <str>
    }
    """
    pids = import_timelogger_pids("timelogger_project_pids.json")
    for item in toggl_data:
        payload = {
            "expectedhours": "8",
            "project_id": pids.get(item.get("contract")),
            "days_spent": "0",
            "hours_spent": "0",
            "minutes_spent": item.get("time_spent_seconds") // 60,
            "comments": item.get("description"),
            "reference": "",
            "create": "Log",
        }
        date = item.get("date").split("T")[0]
        url = f"https://extranet.opusvl.com/modules/timelogger/entries/add_time_entry/{username}/{date}"
        with login() as session:
            session.post(url, data=payload, auth=auth)


def import_timelogger_pids(filename: str) -> dict:
    """
    The imported file needs to be in the format:
    [
        {"timelogger_pid": "123", "project_name": "Project 1"},
        {"timelogger_pid": "456", "project_name": "Project 2"},
        ...
    ]
    """
    with open(filename, "r") as file:
        data = json.load(file)
    pids = dict()
    for item in data:
        pids[item.get("project_name")] = item.get("timelogger_pid")

    return pids
