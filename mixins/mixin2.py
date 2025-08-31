import json
from typing import Self
from pathlib import Path
from types import SimpleNamespace

class JSONSerializableMixin:
    @classmethod
    def from_json(cls, json_string: str) -> Self:
        return cls(**json.loads(json_string))
    
    def as_json(self) -> str:
        return json.dumps(vars(self))
    
class AppSettings(JSONSerializableMixin, SimpleNamespace):
    def save(self, filepath: str | Path) -> None:
        Path(filepath).write_text(self.as_json(), encoding="utf-8")

def main():
    settings = AppSettings()
    settings.host = "localhost"
    settings.port = 8080
    settings.debug_mode = True
    settings.log_file = None
    settings.urls = (
        "https://192.168.1.200:8000",
        "https://192.168.1.201:8000",
    )
    settings.save("settings.json")

if __name__ == "__main__":
    main()
