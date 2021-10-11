import requests
import json

from configparser import ConfigParser
from datetime import datetime, timedelta

CONFIG = ConfigParser()
CONFIG.read("config.ini")


def get_formatted_data(date: str) -> list:
    data = list()
    time_entries = get_time_entries(date)
    for entry in time_entries:
        project = get_project(entry.get("pid"))
        formatted_entry = {
            "contract": project.get("data", {}).get("name"),
            "description": entry.get("description"),
            "time_spent_seconds": entry.get("duration"),
            "date": entry.get("start"),
        }
        data.append(formatted_entry)
    return data


def get_time_entries(date: str):
    start_date = datetime.strptime(date.replace("/", "-"), "%Y-%m-%d")
    end_date = start_date + timedelta(hours=23, minutes=59, seconds=59)
    start_date = start_date.astimezone().isoformat()
    end_date = end_date.astimezone().isoformat()
    url = "https://api.track.toggl.com/api/v8/time_entries"
    params = {
        "start_date": start_date,
        "end_date": end_date,
    }
    response = toggl_request_get(url, params)
    return json.loads(response.text)


def toggl_request_get(url: str, params: dict = False) -> requests.Response:
    """Send a GET request to specified url using toggl headers and configured auth"""
    headers = {"Content-Type": "application/json"}
    auth = (CONFIG["toggl"]["api_token"], "api_token")
    response = requests.get(url, headers=headers, auth=auth, params=params)
    return response


def get_project(project_id: int) -> dict:
    """Return project details for given project number"""
    if project_id:
        base_url = "https://api.track.toggl.com/api/v8/projects/"
        api_url = base_url + str(project_id)
        response = toggl_request_get(api_url)
        return json.loads(response.text)
    return {}
