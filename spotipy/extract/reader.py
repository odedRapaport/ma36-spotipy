from abc import ABC, abstractmethod
import json


class Reader(ABC):
    @abstractmethod
    def read(self):
        pass


class JsonReader(Reader):
    def __init__(self, path: str):
        self.path = path

    def read(self):
        with open(self.path) as json_file:
            return json.load(json_file)


def config_read():
    return JsonReader("configuration.json").read()
