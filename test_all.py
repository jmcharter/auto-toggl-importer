import timelogger
import toggl
import json


def test_config():
    username = timelogger.CONFIG["opusvl"]["username"]
    password = timelogger.CONFIG["opusvl"]["password"]
    api_token = timelogger.CONFIG["toggl"]["api_token"]
    assert type(username) == str and username != ""
    assert type(password) == str and password != ""
    assert type(api_token) == str and api_token != ""


def test_toggl_request_get():
    url = "https://api.track.toggl.com/api/v8/me"
    res = toggl.toggl_request_get(url)
    data = json.loads(res.text)
    fullname = data.get("data").get("fullname")

    assert type(fullname) == str and fullname != ""


def test_toggle_get_project():
    url = "https://api.track.toggl.com/api/v8/me?with_related_data=true"
    projects = json.loads(toggl.toggl_request_get(url).text).get("data").get("projects")
    project_one = projects[0].get("id")
    res = toggl.get_project(project_one)

    assert project_one == res.get("data").get("id")
