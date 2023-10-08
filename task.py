from dataclasses import dataclass
from datetime import datetime

@dataclass
class Task:

    id: str
    name: str
    type: str
    description: str
    deadline: datetime
    persons: []
    creator_id: str
    notify: bool