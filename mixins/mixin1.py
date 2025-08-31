import json
from dataclasses import dataclass
from datetime import date

class JSONSerializableMixin:
    def as_json(self) -> str:
        return json.dumps(vars(self))
    

@dataclass
class User(JSONSerializableMixin):
    user_id: int
    email: str

def main():
    print(User(123, "user@example.org").as_json())

if __name__ == "__main__":
    main()
