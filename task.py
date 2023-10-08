from dataclasses import dataclass
from datetime import datetime

@dataclass
class Task:
    id: str
    name: str
    type: str
    description: str
    deadline: datetime
    persons: list
    creator_id: str
    completed: bool
    notify: bool