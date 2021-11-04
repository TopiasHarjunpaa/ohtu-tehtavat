from urllib import request
from project import Project
import toml


class ProjectReader:
    def __init__(self, url):
        self._url = url

    def get_project(self):
        content = request.urlopen(self._url).read().decode("utf-8")
        parsed_content = toml.loads(content)["tool"]["poetry"]

        return Project(parsed_content["name"], parsed_content["description"], parsed_content["dependencies"], parsed_content["dev-dependencies"])
