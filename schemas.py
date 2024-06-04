from pydantic import BaseModel

class Address(BaseModel):
    street: str
    city: str
    zip: str    

class User(BaseModel):
    name: str
    email: str
    address: Address

class Report(BaseModel):
    title: str
    content: str