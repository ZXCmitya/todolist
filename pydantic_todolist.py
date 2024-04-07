from pydantic import *

class Task(BaseModel):
    id: int
    task: str
    completed: int