from pydantic import BaseModel

class Course(BaseModel):
    name: str
    description: str
    type: bool

class Group(BaseModel):
    members: list

