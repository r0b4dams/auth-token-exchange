import json

with open('./project.json') as data:
    project_data = json.load(data)

project_data["app_name"] = "-".join(
    [project_data["name"], project_data["version"]])
